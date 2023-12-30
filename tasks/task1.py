from celery_app import celery

@celery.task(name='votre_projet.task1')
def task1(values):
     return values
