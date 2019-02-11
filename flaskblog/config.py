import os


class Config:
    SECRET_KEY = ('eb2c4dec5b0caef0c83d582a205edcb79bf797c0ac')
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nakalanziJacklyn98@gmail.com'
    MAIL_PASSWORD = '0784582081kirabs'


# SECRET_KEY = os.environ.get('SECRETS_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('EMAIL_USER')
#     MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
