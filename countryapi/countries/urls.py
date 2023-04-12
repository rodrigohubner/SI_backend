from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, ContinentViewSet
from . import views


router = DefaultRouter()
router.register(r"countries", CountryViewSet)
router.register(r"continents", ContinentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', views.index, name='index'),
    path('continents/', views.index, name='index'),
]