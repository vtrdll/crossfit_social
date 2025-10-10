
import os
from django.contrib.auth.models import User
from django.db.utils import OperationalError



from .celery import app as celery_app

__all__ = ('celery_app',)


