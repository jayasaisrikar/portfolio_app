from .settings import *

# Use in-memory SQLite database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable debugging for tests
DEBUG = False

# Use a faster password hasher during tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Use temporary folder for media files during tests
import tempfile
MEDIA_ROOT = tempfile.mkdtemp() 