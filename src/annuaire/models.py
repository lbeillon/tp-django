from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=10)
    entreprise = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.telephone}"



