from os import name
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here


class Details(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Document(models.Model):
    fileformat = models.FileField(
        upload_to="documents/",
        validators=[
            FileExtensionValidator(allowed_extensions=["zip"]),
        ],
    )
