import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Make sure this matches the actual name of your project folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_wsgi_application()

# Update the path below if needed
application = WhiteNoise(application, root='/home/jjmljuma/myportfolio/staticfiles')
