from rest_framework import serializers
from .models import SparePart, CarModel


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = CarModel
        fields = ['manufacturer', 'model', 'year']
        
        # Removes validator checks on creating a new spare part.
        validators = []


class SparePartSerializer(serializers.ModelSerializer):

    car_model = CarModelSerializer()

    class Meta:
        model = SparePart
        fields = '__all__'

    def create(self, validated_data):
        car_model_data = validated_data.pop('car_model')
        car_model = None

        try:
            car_model = CarModel.objects.get(
                manufacturer__iexact=car_model_data['manufacturer'],  # ✅ Case-insensitive
                model__iexact=car_model_data['model'],  # ✅ Case-insensitive
                year=car_model_data['year']
            )

        except CarModel.DoesNotExist:
            raise serializers.ValidationError(
                {"car_model": "The specified car model does not exist."})

        spare_part = SparePart.objects.create(car_model=car_model, **validated_data)
        
        return spare_part


    def update(self, instance, validated_data):
        
        car_model_data = validated_data.pop('car_model')
        car_model = None
        
        try:
            car_model = CarModel.objects.get(
                manufacturer__iexact=car_model_data['manufacturer'],  # ✅ Case-insensitive
                model__iexact=car_model_data['model'],  # ✅ Case-insensitive
                year=car_model_data['year']
            )
        except CarModel.DoesNotExist:
            raise serializers.ValidationError(
                {"car_model": "The specified car model does not exist."})
        
        instance.car_model = car_model
        instance.part_name = validated_data.get('part_name', instance.part_name)
        instance.category = validated_data.get('category', instance.category)
        instance.part_number = validated_data.get('part_number', instance.part_number)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.min_stock = validated_data.get('min_stock', instance.min_stock)
        instance.supplier = validated_data.get('supplier', instance.supplier)
            
        instance.save()
        return instance
        
