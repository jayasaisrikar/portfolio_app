import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

application = get_wsgi_application()
application = WhiteNoise(application)

# Add static files
application.add_files(settings.STATIC_ROOT, prefix='static/')

# Add media files
if os.path.exists(settings.MEDIA_ROOT):
    application.add_files(settings.MEDIA_ROOT, prefix='media/')
