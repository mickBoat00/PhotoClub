from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user-default.png', upload_to='profile_pics')
    bio = models.TextField(default='Your bio, you can update it', null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'