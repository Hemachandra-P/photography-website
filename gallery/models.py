from django.db import models

class Photo(models.Model):

    CATEGORY_CHOICES = [
        ('portrait', 'Portrait'),
        ('landscape', 'Landscape'),
    ]

    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='album/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.category})"
