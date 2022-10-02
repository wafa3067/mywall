from django.contrib import admin

from Wallpapers.models import Categories, WallpapersDetail,Images

# Register your models here.

class ImagesInline(admin.TabularInline):
    model=Images



@admin.register(WallpapersDetail)
class WallpaperAdmin(admin.ModelAdmin):
    inlines=[ImagesInline]
    list_display=['title','favourite']

@admin.register(Categories)
class WallpaperAdmin(admin.ModelAdmin):
    list_display=['id','name']
