from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField() 

    def __str__(self):
        return self.name


class Blog(models.Model):
    title=models.CharField(max_length=200)
    created_by=models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_blogs")
    image=models.ImageField(
        upload_to="uploads"
    )
    description=models.TextField()
    is_private=models.BooleanField()
    created_at=models.DateField()

    def __str__(self):
        return self.title

    






    

    