
from rest_framework import serializers
from Wallpapers.models import Images, WallpapersDetail,Categories

class CategoriesSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=('id','name')


class ImageSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields='__all__'


class WallpaperSerializer(serializers.ModelSerializer):
    categories=CategoriesSerilizers()
    wallpapers=ImageSerilizers(many=True)
    class Meta:
        model=WallpapersDetail
        fields=['categories','id','mainimage','title','favourite','wallpapers']