from rest_framework import serializers
from chambre.models import Activite
from django.contrib.auth.models import User
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'titre', 'type_document', 'fichier', 'membre']

class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ['id', 'nom', 'description', 'date_debut', 'date_fin']

class DocumentChargeSerializer(serializers.Serializer):
    fichier = serializers.FileField()

    def create(self, validated_data):
        document = Document(fichier=validated_data['fichier'])
        document.save()
        return document

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user