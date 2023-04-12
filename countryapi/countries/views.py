from django.shortcuts import render
from django.http import HttpResponse

from markdown import markdown as md

from rest_framework import viewsets

from .models import Country, Continent
from .serializers import CountrySerializer, ContinentSerializer


def index(request):
    return HttpResponse(md("#Alguma coisa inicial"))

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class ContinentViewSet(viewsets.ModelViewSet):
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()