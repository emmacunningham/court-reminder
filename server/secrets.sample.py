# Not dependent on anything from deployment, rather these credentials are used by Flask for basic authentication
# We can fill these in with whatever we want
BASIC_AUTH_USERNAME = ''
BASIC_AUTH_PASSWORD = ''
SECRET_KEY = ''  # Cannot leave empty or server will error; can populate with dummy text for local dev
