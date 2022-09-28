from statistics import mode
from django.db import models


class Tasks(models.Model):

    name = models.CharField(max_length=250)
    is_active  = models.BooleanField(default=False)
    

