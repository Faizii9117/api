from rest_framework import serializers
from app_api.models import UserDetail  

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__' 
