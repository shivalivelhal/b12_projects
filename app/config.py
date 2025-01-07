# database configuration will be present
import os

class Config:
    SQLALCHEMY_DATABASE_URI =os.getenv( 'DATABASE_URL','mysql+pymysql://root:root@localhost/flask12_db_product')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# upper both are class level variable  or static variable