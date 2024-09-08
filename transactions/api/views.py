from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Income
from .serializers import IncomeSerializer

class RegisterIncomeView(generics.CreateAPIView):
  queryset = Income.objects.all()
  serializer_class = IncomeSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class IncomeListView(generics.ListAPIView):
  serializer_class = IncomeSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Income.objects.filter(user=user)
