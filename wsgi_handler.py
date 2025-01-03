import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Run migrations
execute_from_command_line(['manage.py', 'migrate'])

# Get the WSGI application
application = get_wsgi_application()
