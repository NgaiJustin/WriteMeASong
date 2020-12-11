from django.shortcuts import render
from rest_framework import generics
from .models import Pop
from .serializers import PopSerializer

# Create your views here.

def main(request):
    pass

# class PopView(generics.ListAPIView):
#     queryset = Pop.objects.all()
#     serializer_class = PopSerializer