import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# Add static files
application.add_files(settings.STATIC_ROOT, prefix='static/')

# Create superuser
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password=os.environ.get('POSTGRES_PASSWORD')
        )
except Exception as e:
    print(f"Error creating superuser: {e}")
