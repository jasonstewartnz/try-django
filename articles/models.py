from django.db import models

# when this file changes, need to run
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()