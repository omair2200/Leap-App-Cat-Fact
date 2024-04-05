# cat_facts/models.py

from django.db import models

class CatFact(models.Model):
    fact = models.TextField()
    fetched_at = models.DateTimeField(auto_now_add=True)
