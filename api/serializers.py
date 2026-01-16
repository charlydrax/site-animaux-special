#api/serializers.py

from rest_framework import serializers

from .models import Animal

class AnimalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        #fields = ['id','name','image']