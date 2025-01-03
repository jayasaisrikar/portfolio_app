import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Initialize Django
django.setup()

try:
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
except Exception as e:
    print(f"Migration error: {str(e)}")

# Get the WSGI application
application = get_wsgi_application()
