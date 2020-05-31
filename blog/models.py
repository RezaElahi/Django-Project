from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Each class will be a table in the database and its attribute are a field in table
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # we pass the function as default value
    author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many relationship

    def __str__(self):
        return self.title
