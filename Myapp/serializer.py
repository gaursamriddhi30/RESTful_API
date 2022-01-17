from rest_framework import serializers
from .models import trainee

class traineeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= trainee
        #fields = {'name,'age}
        fields = '__all__'