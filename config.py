import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/sunrise-db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'e4e9c822b488b0c741e8616712b415c1')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'a436afdbade6c5ae255289d8aa80103adbd4f622b4a99077bb40ac9140b8368a')
