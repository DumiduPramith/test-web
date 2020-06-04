from django.db import models
from django.utils import timezone
# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(default= timezone.now)

    def __str__(self):
        return '{}'.format(self.search)
    
    class Meta:
        verbose_name_plural = 'Searchess'