import os
import sys

# Insert the application directory into sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Load environment variables from the .env file in the project root
# (cPanel shared hosting has no shell to export env vars).
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gogap_web.settings')

# Initialize WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
