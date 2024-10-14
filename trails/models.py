from django.db import models


class Trail(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    description = models.TextField()
    background_image = models.ImageField(upload_to='trail_backgrounds/', null=True)

    def __str__(self):
        return self.name
