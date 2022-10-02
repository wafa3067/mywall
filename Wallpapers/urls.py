from django.urls import path
from .views import WallpapersListApiView
# route=routers.DefaultRouter()
# route.register('wall',WallpapersListApiView)

urlpatterns=[
    path('papers/',WallpapersListApiView.as_view()),
]