from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #permet de definir notre modele(ce qui est un object)
                          #class : indique que nous sommes en train de définir un object
                          #Post : Nom de notre modele
                          #models.Model signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #lien vers un autre modele
    title = models.CharField(max_length=200) #champ texte avec un nombre limité de caracteres
    text = models.TextField() #champ texte sans limite de caracteres
    created_date = models.DateTimeField(default=timezone.now) #champ horodatage(date et heure)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #La règle de nommage est d'utiliser des minuscules et des tirets bas à la place des espaces
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title