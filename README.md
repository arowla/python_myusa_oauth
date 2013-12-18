python_myusa_oauth
==================

A Python oauth2 client for MyUSA. This should work for any popular Python web framework (see docs for python-social-auth), but I'll include instructions for setting up Django to authenticate against MyUSA here.

Django Installation
-------------------

    pip install python-social-auth
    pip install python_myusa_oauth

NOTE: as of 12/18/13, this package isn't actually registered in PyPI yet, so you'll actually need to `git clone` the repository and do an add2virtualenv inside its main directory for the following instructions to work.
Then follow the instructions here for setting up python-social-auth with Django: http://psa.matiasaguirre.net/docs/configuration/django.html

In addition to that, add the MyUSA backend to AUTHENTICATION_BACKENDS in your Django `settings.py`:

    AUTHENTICATION_BACKENDS = (
        ...
        'oauth_myusa.myusa.MyusaOAuth2',
        ...
    )

You'll need to register your app with MyUSA and get a Client ID and a Secret Key. I'll leave it up to you to figure out that part. One hint: by default, the Redirect URI MyUSA will ask you for
will look like "http://<your domain>/done/". Once you've added your app and have your client id and secret, go back into your `settings.py` and add them like so:

    SOCIAL_AUTH_MYUSA_KEY = '<your client id>'
    SOCIAL_AUTH_MYUSA_SECRET = '<your client secret>'

Then, in your app, you can add a login using the provided template tag:

    <a href="{% url 'social:begin' 'myusa' %}">Log in with MyUSA</a>

