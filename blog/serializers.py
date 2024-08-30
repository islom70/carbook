from rest_framework import serializers

from blog.models import Car, Booking


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price']


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'color', 'is_available']


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'color']


class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'color', 'is_available']


class BookCarSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'car', 'start_time', 'end_time']

    def validate(self, data):
        car = data.get('car')
        if not car.is_available:
            raise serializers.ValidationError("This car is not available for booking.")
        return data

    def create(self, validated_data):
        car = validated_data['car']
        car.is_available = False
        car.save()

        booking = Booking.objects.create(**validated_data)

        return booking

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car'] = CarDetailSerializer(instance.car).data
        return representation