# cars/views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # List only cars that belong to the logged-in user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the logged-in user as the owner of the car
        serializer.save(user=self.request.user)
