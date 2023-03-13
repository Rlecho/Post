
from rest_framework import serializers
from .models import Users

class UsersSerialiseur(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('noms', 'adresse', 'email', 'numero')
