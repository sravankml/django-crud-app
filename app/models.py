from django.db import models
from django.utils import timezone
# Create your models here.
class Crud(models.Model):
    content = models.CharField("Type here",max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Crud'
        verbose_name_plural = 'Cruds'