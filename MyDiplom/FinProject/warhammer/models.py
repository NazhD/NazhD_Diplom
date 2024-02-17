from django.db import models
from django.core.validators import FileExtensionValidator


class ImageFile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='warhammer/images/')
    url = models.URLField(blank=True)


class VideoFile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='warhammer/images/')
    url = models.URLField(blank=True)
    file = models.FileField(
        upload_to='warhammer/video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_video = models.DateTimeField(auto_now_add=True)
