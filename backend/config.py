import os
from decouple import config

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Chapanobi2024!')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # postgresql://e_commerce_db_e0tc_user:AT62j7i4fAuegApvbqZRJFuf0iDBXilF@dpg-cqbiri6ehbks73dp92ag-a.oregon-postgres.render.com/e_commerce_db_e0tc
    SQLALCHEMY_TRACK_MODIFICATIONS = False
