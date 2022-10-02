from unicodedata import category
from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name


class WallpapersDetail(models.Model):
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,related_name='category')
    title=models.CharField(max_length=255)
    mainimage=models.ImageField(upload_to='images/',blank=False,null=False)
    favourite=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

class Images(models.Model):
    image=models.ImageField(upload_to='images/')
    wallpapers=models.ForeignKey(WallpapersDetail,on_delete=models.CASCADE,related_name='wallpapers',null=True)
