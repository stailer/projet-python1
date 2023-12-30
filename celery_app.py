from celery import Celery

# Configuration de Celery
celery = Celery('votre_projet',
                broker='redis://redis:6379/0',
                backend='redis://redis:6379/0')

# Importer les tâches Celery
from tasks import task1

