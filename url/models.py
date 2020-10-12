from django.db import models

# Create your models here.
class Shorturl(models.Model):
    sno = models.AutoField(primary_key = True)
    label = models.CharField(max_length=500)
    ori_url = models.CharField(max_length=500)
    uni_key = models.CharField(max_length=50, null=True)
    short_url = models.CharField(max_length=500)
    def __str__(self):
        return self.short_url