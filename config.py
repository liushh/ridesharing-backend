import logging
import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bots.db'
    CORS_ORIGIN = 'http://bots.wizeline.com'
    APPLICATION_DOMAIN = 'your-front-end-domain'

    LOGGING_CONF = 'logging.json'
    LOGGING_LEVEL = logging.INFO

    AUTH0_CLIENT_ID = 'your-client-id'
    AUTH0_CLIENT_SECRET = 'your-secret'
    AUTH0_AUDIENCE = 'your-audience'
    AUTH0_ISSUER = 'https://<your-username>.auth0.com/'
    AUTH0_DOMAIN = '<your-username>.auth0.com'
    AUTH0_CONNECTION = 'your-auth0-connection-name'
    AUTH0_RESULT_URL = 'your-front-end-url'


class Development(Config):
    CORS_ORIGIN = os.environ.get('CORS_ORIGIN')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
    AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
    AUTH0_ISSUER = os.environ.get('AUTH0_ISSUER')
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')


class Local(Config):
    CORS_ORIGIN = os.environ.get('CORS_ORIGIN')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
    AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
    AUTH0_ISSUER = os.environ.get('AUTH0_ISSUER')
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    CORS_ORIGIN = 'http://localhost'

    AUTH0_CLIENT_ID = 'theidentifier'
    AUTH0_CLIENT_SECRET = 'thesecret'
    AUTH0_AUDIENCE = 'theaudience'
    AUTH0_ISSUER = 'theissuer'
    AUTH0_DOMAIN = 'liushh.auth0.com'
    AUTH0_CONNECTION = 'database-connection'
    AUTH0_RESULT_URL = 'https://bots.wizeline.com'
