import os

from flask import Config

class Config(Config):
    enable_utc = True
    APP_NAME = "app"
    MONGODB_DB = os.getenv("MONGODB_DB", "api")
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME", "root")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD", "root")
    MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
    MONGODB_PORT = 27017
    JWT_SECRET_KEY = "asjkdfhlasdjfkljaklsdjflkjasd;lf"
    ERROR_404_HELP = False
    AWS_BUCKET_NAME="fx-offline-demo"