from django.contrib import admin
from django.urls import path, include
from app_api.views import UserViewSet, item_list_view  
from rest_framework import routers

# Initialize the Default Router
router = routers.DefaultRouter()
router.register('UserDetail', UserViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include(router.urls)), 
    path('UserDetails/items/', item_list_view, name='item-list-view'),
]
