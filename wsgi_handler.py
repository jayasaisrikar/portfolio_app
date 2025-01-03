import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

application = get_wsgi_application()

# Configure WhiteNoise
if not settings.DEBUG:
    application = WhiteNoise(application, root=settings.STATIC_ROOT)
    application.add_files(settings.STATIC_ROOT, prefix='static/')
