from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.config.settings')

# Create a Celery instance
app = Celery('apps')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()


## celery -A apps worker --loglevel=info iniciate worker


###celery -A apps beat --loglevel=info  programing tasks
