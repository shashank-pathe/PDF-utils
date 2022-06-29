from django.db import models

# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=200)
    pdf_file = models.FileField()
    
