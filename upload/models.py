from django.db import models

# Create your models here.


class UploadFileModel (models.Model):
    file = models.FileField(null=True)

    def __str__(self):

        return self.file




