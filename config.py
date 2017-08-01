class Config:
    CORS_ORIGIN = '*'

    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/'


class Local(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://liusha@localhost/sample'


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://liusha:12345@/postgres?host=/cloudsql/liusha-hello-world:us-west1:postgre'
