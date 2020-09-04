from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """A post for everyone to see with a pic, description and comments"""
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(default='test_pic.png', blank=True)
    description = models.CharField(max_length = 500)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """return string representation of model"""
        return self.description