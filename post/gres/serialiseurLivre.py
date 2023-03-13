
from rest_framework import serializers
from .models import Livres

class LivreSerialiseur(serializers.ModelSerializer):
    class Meta:
        model = Livres
        fields = ('titre', 'auteur', 'date_publication', 'quantite')


        