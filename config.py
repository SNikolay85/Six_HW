import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS=os.getenv('ALLOWED_HOSTS')
DB_NAME=os.getenv('cicd')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
