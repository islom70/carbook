from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from blog.models import Car, Booking
from blog.serializers import CarListSerializer, CarDetailSerializer, CarCreateSerializer, CarUpdateSerializer, \
    BookCarSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.filter(is_available=True)
    serializer_class = CarListSerializer
    permission_classes = [AllowAny]


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer


class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer


class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()


class BookCarAPIView(generics.CreateAPIView):
    serializer_class = BookCarSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookedCarListApiView(generics.ListAPIView):
    serializer_class = BookCarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)