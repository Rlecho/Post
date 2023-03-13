from rest_framework import serializers
from .models import Emprunts

from .serialiseurLivre import LivreSerialiseur
from .serialiseurUsers import UsersSerialiseur

class EmpruntsSerialiseur(serializers.ModelSerializer):
    class Meta:
        model = Emprunts
        fields = ('livre', 'user', 'date_emprunt', 'date_retour')


        