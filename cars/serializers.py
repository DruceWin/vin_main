from rest_framework import serializers

from .models import Car, Photos


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('year', 'brand', 'model', 'vin', 'odometer',
                  'engine', 'gearbox', 'drive_train', 'auction_date',
                  'sale_type', 'damage', 'photo')


class VinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin',)

    # def to_representation(self, instance):
    #     return f'https://vinbenzin.info/catalogue/{instance.vin}'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'
