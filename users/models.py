from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    userBugs = models.IntegerField(default=0)
    userCompletedBugs = models.IntegerField(default=0)
    greenBugs = models.IntegerField(default=0)
    yellowBugs = models.IntegerField(default=0)
    redBugs = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
