import os


DB_FILE = os.path.join(os.path.dirname(__file__), 'database.sqlite')

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'this-is-a-secret-key'
    # @staticmethod
    # def init_app(app):
    #     pass  # Additional initialization can be done here if needed