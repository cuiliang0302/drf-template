from DRF.settings.base import *
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 200,
        }
    }
}