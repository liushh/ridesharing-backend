import random
import string

import requests

class Auth0Error(Exception): pass               # noqa
class Auth0UserDoesNotExists(Exception): pass   # noqa
class Auth0InvalidCredentials(Exception): pass  # noqa
class Auth0UserAlreadyCreated(Exception): pass  # noqa


def first(array):
    return array[0]


class Auth0Authenticator:
    def __init__(self, domain, client_id, client_secret, access_token=None, token_type='Bearer'):
        self.domain = domain
        self.client_id = client_id
        self.client_secret = client_secret

        self._access_token = access_token
        self._token_type = token_type

    def refresh_token(self):
        self._token_type, self._access_token = self._issue_auth0_api_token()

    def get_access_token(self):
        if not self._has_access_token():
            self.refresh_token()

        return self._token_type, self._access_token

    def _has_access_token(self):
        return self._access_token is not None

    def _issue_auth0_api_token(self):
        url = 'https://' + self.domain + '/oauth/token'
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'audience': 'https://' + self.domain + '/api/v2/'
        }

        response = requests.post(url, json=payload)

        if self._has_error(response):
            raise Auth0InvalidCredentials

        token_data = response.json()
        return token_data['token_type'], token_data['access_token']

    def _has_error(self, response):
        return response.status_code != 200


class Auth0Gateway:
    PASSWORD_LENGTH = 10

    def __init__(self, domain, authenticator):
        self.domain = domain
        self.authenticator = authenticator

    def get_user(self, auth0_id):
        url = 'https://' + self.domain + '/api/v2/users/' + auth0_id
        return self._fetch_user(url)

    def _fetch_user(self, url, should_retry=True):
        response = requests.get(url, headers={
            'Authorization': self._get_authorization_header()
        })

        if self._has_error(response):
            if self._is_not_found(response):
                raise Auth0UserDoesNotExists

            if self._is_invalid_token(response):
                if should_retry:
                    print('refetching the authentication token from auth0')
                    self.authenticator.refresh_token()
                    return self._fetch_user(url, False)
                raise Auth0InvalidCredentials

            raise Auth0Error
        return response.json()

    def _get_authorization_header(self):
        token_type, access_token = self._get_access_token()
        return token_type + " " + access_token

    def _get_access_token(self):
        return self.authenticator.get_access_token()

    def _has_error(self, response):
        return response.status_code != 200

    def _is_not_found(self, response):
        return response.status_code == 404

    def _is_invalid_token(self, response):
        return response.status_code == 401
