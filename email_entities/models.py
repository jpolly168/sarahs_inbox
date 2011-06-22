from django.db import models
from mail.models import *
from dcentity.models import *

#This is for building the database of associations. In the future we should probably just connect
#the inbox up to the transparency data api or something similar.
class EmailEntity(models.Model):
    mail            = models.ForeignKey('mail.Email',on_delete=models.PROTECT, related_name="related_entity")
    entity          = models.CharField(max_length=128)
    entity_name     = models.CharField(max_length=256)
    entity_type     = models.CharField(max_length=128)
    references      = models.TextField()
    party           = models.CharField(max_length=128)

class EmailEntityIndustry(models.Model):
    industry    = models.CharField(max_length=128)
    entity      = models.ForeignKey(EmailEntity)