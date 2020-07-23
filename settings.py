import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
PORT = os.environ.get('POSTGRES_PORT')
DB = os.environ.get('POSTGRES_DB')
SERVER = os.environ.get('POSTGRES_SERVER')
DATABASE_URL_DOCKER = f'postgresql+psycopg2://{USER}:{PASSWORD}@{SERVER}:{PORT}/{DB}'
print(DATABASE_URL_DOCKER)
