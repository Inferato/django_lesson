import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

app = Celery(
    'test_project'
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
