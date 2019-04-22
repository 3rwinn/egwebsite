from django.db import models
from datetime  import datetime

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technology_used = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    image_main = models.ImageField(upload_to='images/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    project_type = models.CharField(max_length=200)
    project_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name



