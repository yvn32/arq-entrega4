from django.db import models

class cuenta(models.Model):
  correo = models.CharField(max_length=70)
  pwd = models.CharField(max_length=20)

