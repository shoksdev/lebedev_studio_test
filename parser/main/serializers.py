from rest_framework import serializers

from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода информации обо всех событиях"""

    class Meta:
        model = Event
        fields = ('institution', 'region', 'address', 'year', 'budget_amount')
