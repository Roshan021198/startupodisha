from django.db import models

# Create your models here.
class IndustryPartner(models.Model):
    logo_img            = models.FileField(upload_to='logo',null=True,blank=True)