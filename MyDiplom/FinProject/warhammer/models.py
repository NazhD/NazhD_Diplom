from django.db import models


class ImageFile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='warhammer/images/')
    url = models.URLField(blank=True)
