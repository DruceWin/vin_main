from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('year', 'brand', 'model', 'vin', 'odometer',
                  'engine', 'gearbox', 'drive_train', 'auction_date',
                  'sale_type', 'damage', 'photo', 'is_hidden', 'is_hidden_v2')


class VinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin',)
