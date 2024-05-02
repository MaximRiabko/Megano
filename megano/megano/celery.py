import os
from celery import Celery
from megano.megano.settings import ON_PAYMENT
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'megano.settings')

if ON_PAYMENT:
    app = Celery('payment')
    app.config_from_object('django.conf.settings', namespace='CELERY')
    app.autodiscover_tasks()
