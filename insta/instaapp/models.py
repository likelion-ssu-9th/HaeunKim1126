from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class instagram(models.Model):
    writer = models.ForeignKey(User, related_name="post", on_delete=CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

def __str__(self) :
    return self.title
    



# Create your models here.
#class Instas (models.Model):
    adress = models.CharField(max_length=10)
    userpassword = models.CharField(max_length=20)


#def __str__(self):
    return self.userID


 #userName = models.CharField(max_length=15)
    userID = models.CharField(max_length=20,unique = True)
    feedimage = models.ImageField(blank = True , upload_to='feed.html')
    feedtext = models.TextField(blank=True)
    profileimage = models.ImageField(blank = True , upload_to='profile.html')
    created_db = models.DateTimeField(auto_now_add = True)