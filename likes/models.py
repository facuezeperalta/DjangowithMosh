from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class LikedItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    content_type = models.ForeignKey(ContentType,on_delete = models.CASCADE)  #type of object that the users likes
    object_id = models.PositiveIntegerField() #if the object_is is not a integer will throw an error.
    content_object = GenericForeignKey() #the object itself.

