import os
import logging


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
    CORS_ORIGIN = '*'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:hls901021@/postgres?host=/cloudsql/liusha-hello-world:us-west1:wizepool'
    AUTH0_CLIENT_ID = 'f4to0gzhJ4eWYx7MaquQdPFxu873B5Pc'
    AUTH0_CLIENT_SECRET = 'HLYF-N5JCdpN9viGqhmD1dAKljnJr7wpdxbLiwljMiSdx0PVmYiMQ2F4KbPnsyYC'
    AUTH0_AUDIENCE = 'f4to0gzhJ4eWYx7MaquQdPFxu873B5Pc'
    AUTH0_ISSUER = 'https://liushh.auth0.com/'
    AUTH0_DOMAIN = 'liushh.auth0.com'


class Local(Config):
    CORS_ORIGIN = '*'
    SQLALCHEMY_DATABASE_URI = 'postgresql://liusha@localhost/sample'
    AUTH0_CLIENT_ID = 'f4to0gzhJ4eWYx7MaquQdPFxu873B5Pc'
    AUTH0_CLIENT_SECRET = 'HLYF-N5JCdpN9viGqhmD1dAKljnJr7wpdxbLiwljMiSdx0PVmYiMQ2F4KbPnsyYC'
    AUTH0_AUDIENCE = 'f4to0gzhJ4eWYx7MaquQdPFxu873B5Pc'
    AUTH0_ISSUER = 'https://liushh.auth0.com/'
    AUTH0_DOMAIN = 'liushh.auth0.com'


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
