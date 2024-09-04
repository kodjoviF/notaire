from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Activite
from ..notaires.serializers import ActiviteSerializer


class ActiviteListAPIView(APIView):
    def get(self, request):
        activites = Activite.objects.all()
        serializer = ActiviteSerializer(activites, many=True)
        return Response(serializer.data)