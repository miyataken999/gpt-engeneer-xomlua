INSTALLED_APPS = [
    # ...
    'handbags.apps.HandbagsConfig',
    # ...
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'billingham_handbags.db',
    }
}