
from .serializers import ConvitesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, CreateAPIView
from .models import Convites
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

class IsOwer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.remetente == request.user
    
class CreateConvite(CreateAPIView):
    serializer_class = ConvitesSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(remetente=self.request.user)

class DeleteConvite(DestroyAPIView):
    queryset = Convites.objects.all()
    serializer_class = ConvitesSerializer
    permission_classes = [IsAuthenticated, IsOwer]
    lookup_field = 'id'