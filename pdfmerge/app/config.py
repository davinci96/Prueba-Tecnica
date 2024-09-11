from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config:
    SECRET_KEY    = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'app/utils/files/temp/'