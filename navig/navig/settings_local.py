DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'oxero',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL  = ''
#SERVER_EMAIL       = ''
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
