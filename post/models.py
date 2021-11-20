from django.db import models
from django.db.models.fields import BooleanField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone
# Create your models here.




class Post(models.Model):
    name = models.CharField(max_length=50)
    content =  models.TextField(max_length=50)
    craet_at = models.DateTimeField(default=timezone.now())
    image =   models.ImageField(upload_to='images' )
    active = BooleanField(default=False)
    
    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name

 