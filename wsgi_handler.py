import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

try:
    execute_from_command_line(['manage.py', 'migrate'])
except Exception as e:
    print(f"Migration error: {str(e)}")

application = get_wsgi_application()
application = WhiteNoise(
    application,
    root=os.path.join(settings.BASE_DIR, 'staticfiles'),
    prefix='/'
)

# Add files from STATICFILES_DIRS
for static_dir in settings.STATICFILES_DIRS:
    application.add_files(static_dir, prefix='static/')
