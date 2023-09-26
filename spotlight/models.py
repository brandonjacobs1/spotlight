import os.path

from django.db import models
from spotlight.storage_backends import PrivateMediaStorage


# Create your models here.
class Spotlight(models.Model):
    def spotlight_image_upload_path(self, filename):
        # Customize the upload path based on instance attributes
        name, extension = os.path.splitext(filename)
        return f'{self.last_name}_{self.first_name_husband}_{self.first_name_wife}{extension}'

    last_name = models.CharField(max_length=20, default=None, blank=True, null=True)
    first_name_husband = models.CharField(max_length=20, default=None, blank=True, null=True)
    first_name_wife = models.CharField(max_length=20, default=None, blank=True, null=True)
    statusChoices = (('NS', 'Not Started'), ('A', 'Asked'), ('R', 'Ready'), ('P', 'Planned'), ('S', 'Slacked'))
    status = models.CharField(max_length=2, choices=statusChoices, default='NS', blank=True, null=True)
    date_asked = models.DateField(default=None, blank=True, null=True)
    date_ready = models.DateField(default=None, blank=True, null=True)
    date_planned = models.DateField(default=None, blank=True, null=True)
    date_slacked = models.DateField(default=None, blank=True, null=True)
    member_types = (
        ('O', 'Old'),
        ('N', 'New'),
        ('W', 'Ward Council')
    )
    member_type = models.CharField(max_length=1, choices=member_types, default='O', blank=True, null=True)
    date_joined = models.DateField(default=None, blank=True, null=True)
    bio = models.TextField(default=None, blank=True, null=True)
    image = models.ImageField(storage=PrivateMediaStorage(), default=None, upload_to=spotlight_image_upload_path, blank=True, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name_husband} and {self.first_name_wife}'


