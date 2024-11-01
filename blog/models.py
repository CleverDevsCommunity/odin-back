from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    view_count = models.IntegerField(default=0)
    title = models.CharField(max_length=100 , null=True)
    time_created = models.TimeField(auto_now=True , null=False)
    description = models.CharField(max_length=250 ,null=True)
    body = models.TextField(max_length=10000 , null=False)
    image = models.ImageField(upload_to='pics/' , default="pics/placeholder.png" , null=True)
    date = models.DateField(null=False , default=datetime.now)