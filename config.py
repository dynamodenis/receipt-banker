class Config:
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://dynamodenis:den28041997is@localhost/banker'
    DEBUG=True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}