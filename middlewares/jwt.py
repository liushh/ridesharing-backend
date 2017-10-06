import jwt
import falcon

from sqlalchemy.exc import IntegrityError

from domain.auth0 import (
    Auth0Authenticator,
    Auth0Gateway,
    Auth0UserDoesNotExists,
    Auth0InvalidCredentials
)

from models import User


class InvalidPayload(Exception): pass           # noqa
class UserNotRegistered(Exception): pass        # noqa
class UserAlreadyRegistered(Exception): pass    # noqa


class JWTMiddleware:
    def __init__(self, database, secret, audience, issuer, user_creator=None):
        self.database = database
        self.secret = secret
        self.audience = audience
        self.issuer = issuer
        self.algorithms = 'HS256'
        self.user_creator = user_creator

    def process_resource(self, req, resp, resource, params):
        is_public_resource = getattr(resource, 'is_public', False)
        if is_public_resource:
            return

        token = req.get_header('Authorization')

        if not token:
            raise falcon.HTTPUnauthorized('No auth token found')

        try:
            payload = self._decode_token(token)
            auth0_id = self._get_user_id(payload)
        except jwt.ExpiredSignatureError:
            raise falcon.HTTPUnauthorized('Token has expired')
        except jwt.InvalidAudienceError:
            raise falcon.HTTPUnauthorized('Auth audience is not valid')
        except jwt.InvalidIssuerError:
            raise falcon.HTTPUnauthorized('Auth issuer is not valid')
        except (jwt.InvalidTokenError, InvalidPayload):
            raise falcon.HTTPUnauthorized('Auth token is not valid')

        with self.database.session() as session:
            try:
                req.current_user = self._find_user_by_auth0_id(session, auth0_id)
            except UserNotRegistered:
                req.current_user = self._create_user(session, auth0_id)

        return req.current_user

    def _create_user(self, session, auth0_id):
        if not self._can_create_users():
            print('cannot create a user')
            raise falcon.HTTPUnauthorized('Auth token is not valid')

        try:
            return self.user_creator.create(session, auth0_id)
        except UserAlreadyRegistered:
            return self._find_user_by_auth0_id(session, auth0_id)
        except Auth0InvalidCredentials:
            raise falcon.HTTPUnauthorized('Can not validate token on Auth0')
        except Auth0UserDoesNotExists:
            raise falcon.HTTPUnauthorized('User does not exists on Auth0')

    def _can_create_users(self):
        return self.user_creator is not None

    def _decode_token(self, token):
        return jwt.decode(
            token,
            self.secret,
            audience=self.audience,
            issuer=self.issuer,
            algorithms=[self.algorithms]
        )

    def _get_user_id(self, payload):
        if 'sub' not in payload:
            print('sub is not found')
            raise InvalidPayload

        return payload['sub']

    def _find_user_by_auth0_id(self, session, auth0_id):
        user = session.query(User) \
            .filter(User.auth0_id == auth0_id) \
            .one_or_none()

        if user is not None:
            return user

        raise UserNotRegistered

class Auth0UserCreator:
    def __init__(self, domain, client_id, client_secret, access_token=None, token_type='Bearer'):
        authenticator = Auth0Authenticator(
            domain,
            client_id,
            client_secret,
            access_token=access_token,
            token_type=token_type
        )

        self.auth0_gateway = Auth0Gateway(domain, authenticator)

    def create(self, session, auth0_id):
        user_profile = self._fetch_user_profile(auth0_id)

        try:
            user = User(
                username=user_profile['nickname'],
                email=user_profile['email'],
                auth0_id=auth0_id
            )
            session.save(user)
            print('user is saved ', user)
        except IntegrityError:
            raise UserAlreadyRegistered

        return user

    def _fetch_user_profile(self, auth0_id):
        return self.auth0_gateway.get_user(auth0_id)
