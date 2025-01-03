import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
application = get_wsgi_application()

try:
    django.setup()
    execute_from_command_line(['manage.py', 'migrate'])
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', os.environ.get('ADMIN_PASSWORD', 'admin'))
except Exception as e:
    print(f"Setup error: {str(e)}")
