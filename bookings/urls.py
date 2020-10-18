from django.urls import path

import bookings.views

app_name = 'bookings'
urlpatterns = [
    path('', bookings.views.ApiBookingCreateView.as_view(), name='create'),
]
