import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# username = os.environ.get("USERNAME")
# password = os.environ.get("PASSWORD")
# rds_endpoint = os.environ.get("RDS_ENDPOINT")
# rds_port = os.environ.get("PORT")
# rds_database_name = os.environ.get("DATABASE_NAME")
class Config:
    SECRET_KEY = os.environ.get("SECRET")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{rds_endpoint}:{rds_port}/{rds_database_name}"
    # print(os.environ.get("DATABASE_URL")[11:])
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ.get("DATABASE_URL")[11:]}'
