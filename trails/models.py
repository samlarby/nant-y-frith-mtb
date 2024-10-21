from django.db import models

# model for adding trails 
class Trail(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    description = models.TextField()
    background_image = models.ImageField(upload_to='trail_backgrounds/', null=True)

    def __str__(self):
        return self.name

# model for adding feature images to each trail
class TrailFeatureImage(models.Model):
    trail = models.ForeignKey(Trail, related_name='feature_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trail_features/', null=True)

    def __str__(self):
        return f"{self.trail.name} Feature Image"