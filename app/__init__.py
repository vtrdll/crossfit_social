
import os
from django.contrib.auth.models import User
from django.db.utils import OperationalError



from .celery import app as celery_app

__all__ = ('celery_app',)



def create_default_superuser():
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@meusite.com',
                password='Curitiba@2'
            )
            print("Superuser criado!")
    except OperationalError:
        # Isso evita erro se o banco ainda não estiver migrado
        pass

create_default_superuser()