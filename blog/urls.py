from django.urls import path
from blog.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, BookCarAPIView, \
    BookedCarListApiView

urlpatterns = [
    path('list/', CarListView.as_view(), name='car_list'),
    path('detail/<int:pk>/', CarDetailView.as_view(), name='car_list'),
    path('create/', CarCreateView.as_view(), name='car_list'),
    path('update/<int:pk>/', CarUpdateView.as_view(), name='car_list'),
    path('delete/<int:pk>/', CarDeleteView.as_view(), name='car_list'),
    path('book/', BookCarAPIView.as_view(), name='booking'),
    path('mybookings/', BookedCarListApiView.as_view(), name='mybookings')
]