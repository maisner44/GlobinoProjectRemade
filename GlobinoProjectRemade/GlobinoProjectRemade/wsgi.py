"""
WSGI config for GlobinoProjectRemade project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from apscheduler.schedulers.background import BackgroundScheduler
from departments.jobs import schedule_api
from django.core.wsgi import get_wsgi_application

scheduler = BackgroundScheduler()
scheduler.add_job(schedule_api, "interval", seconds=60)
scheduler.start()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GlobinoProjectRemade.settings')

application = get_wsgi_application()
