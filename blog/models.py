from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    image =  models.ImageField(upload_to="blog_image/",blank=True,null=True)

    description = models.CharField(max_length=200,default="")

    name = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    body = RichTextUploadingField()
    created_at =  models.TimeField(default=timezone.now())

    def __str__(self):
        return f"{self.title} {self.created_at}"


