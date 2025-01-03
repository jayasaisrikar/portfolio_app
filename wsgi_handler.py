import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Initialize Django
django.setup()

try:
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')).exists():
        User.objects.create_superuser(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'),
            password=os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
        )
except Exception as e:
    print(f"Setup error: {str(e)}")

# Get the WSGI application
application = get_wsgi_application()
