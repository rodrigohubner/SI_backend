from django.contrib import admin
from .models import Continent, Country


admin.site.register((Continent, Country))