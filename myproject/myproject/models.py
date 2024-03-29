from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    class Meta:
        app_label = 'myproject'
    Name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    weight=models.IntegerField()
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'


