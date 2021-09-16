from django.db import models
from django.utils import timezone

# Create your models here.
class todomodel(models.Model):
    task = models.CharField(max_length=255,blank=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.task