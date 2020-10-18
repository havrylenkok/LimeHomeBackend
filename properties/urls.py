from django.urls import path

import properties.views

app_name = 'properties'
urlpatterns = [
    path('', properties.views.ApiPropertyListView.as_view({'get': 'list'}), name='index'),
    path('<str:id>/bookings/', properties.views.ApiPropertyBookingsListView.as_view(), name='bookings')
]
