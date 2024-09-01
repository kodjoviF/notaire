# les serializers agissent comme un pont entre les 
# modèles Django et les formats de données utilisés dans les API REST, 
# facilitant la conversion, la validation et le contrôle des 
# données échangées entre le client et le serveur.





from rest_framework import serializers
from .models import Activite

class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ['id', 'titre', 'date']  # Ajoutez d'autres champs si nécessaire
        
        
        def validate_titre(self, value):
            if len(value) < 5:
                raise serializers.ValidationError("Le titre doit contenir au moins 5 caractères.")
            return value
        
# serialser
        
        
        activite = Activite.objects.get(id=1)
serializer = ActiviteSerializer(Activite)
data = serializer.data  # Données prêtes à être envoyées en JSON


# deserialiser
data = {'titre': 'Nouvelle activité', 'date': '2024-09-15', 'description': 'Description...'}
serializer = ActiviteSerializer(data=data)
if serializer.is_valid():
    serializer.save()  # Crée une nouvelle instance d'Activite
else:
    print(serializer.errors)  # Affiche les erreurs de validation