from django.db import models

class Post(models.Model):
    """A post for everyone to see with a pic, description and comments"""
    image = models.ImageField(null=True)
    description = models.CharField(max_length = 500)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """return string representation of model"""
        return self.description