from django.db import models
class UserDetails(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(null=False)
    display_name=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.username


# Create your models here.
