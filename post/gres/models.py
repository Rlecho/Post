from django.db import models
from django.db import IntegrityError

# Create your models here.
class Livres(models.Model):

    identifiant      = models.IntegerField(primary_key= True, default=0, editable=False)
    titre            = models.CharField(max_length=200)
    auteur           = models.CharField(max_length=200)
    date_publication = models.DateField()
    quantite         = models.IntegerField()
   # image           = models.ImageField(upload_to='chemin/vers/dossier/')


   

class Users(models.Model):

    identifiant = models.IntegerField(primary_key= True, default=0, editable=False)
    noms        = models.CharField(max_length=200)
    adresse     = models.CharField(max_length=200)
    email       = models.EmailField()
    numero      = models.DecimalField(max_digits=10, decimal_places=5)
   # image      = models.ImageField(upload_to='chemin/vers/dossier/')
   
class Emprunts(models.Model):

    identifiant      = models.IntegerField(primary_key= True, default=0, editable=False)
    livre            = models.ForeignKey(Livres, on_delete=models.PROTECT)
    user             = models.ForeignKey(Users, on_delete=models.PROTECT)
    date_emprunt     = models.DateField(auto_now_add=True)
    date_retour      = models.DateField(null=True, blank=True)
   # image           = models.ImageField(upload_to='chemin/vers/dossier/')
        # try:
        #     livre.delete()
        #     user.delete()
        # except IntegrityError:
        #     # gestion de l'exception ici