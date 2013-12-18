from social.backends.oauth import BaseOAuth2

class MyusaOAuth2(BaseOAuth2):
    """ MyUSA OAuth Authentication Backend"""
    name = 'myusa'
    AUTHORIZATION_URL = 'https://my.usa.gov/oauth/authorize'
    ACCESS_TOKEN_URL = AUTHORIZATION_URL

