import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
application = get_wsgi_application()

# Configure WhiteNoise
application = WhiteNoise(
    application,
    root=settings.STATIC_ROOT,
    prefix='static/',
    allow_all_origins=True
)

# Add static files
application.add_files(settings.STATIC_ROOT, prefix='static/')
