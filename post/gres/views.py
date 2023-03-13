from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livres
from .models import Users
from .models import Emprunts
from .serialiseurLivre import LivreSerialiseur
from .serialiseurUsers import UsersSerialiseur
from .serialiseurEmprunts import EmpruntsSerialiseur

# Create your views here.

class LivresListe(APIView):
    def get(self, request):
        livres = Livres.objects.all()
        serializer = LivreSerialiseur(livres, many=True)
        return Response(serializer.data)



class CreateLivres(APIView):
    def post(self, request):
        serializer = LivresSerialiseur(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUsers(APIView):
    def post(self, request):
        serializer = LivresSerialiseur(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LivresEmprunteListe(APIView):
    def get(self, request):
        livres_empruntes = Emprunts.objects.all()
        serializer = EmpruntsSerialiseur(livres_empruntes, many=True)
        return Response(serializer.data)