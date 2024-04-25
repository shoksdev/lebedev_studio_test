from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView

from .models import Event
from .serializers import EventListSerializer


class EventListAPIView(ListAPIView):
    """Вывод списка всех событий из таблицы с возможностью поиска по всем полям"""

    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['institution', 'region', 'address', 'year', 'budget_amount',]
