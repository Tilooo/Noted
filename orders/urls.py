from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/canceled/', views.payment_canceled, name='payment_canceled'),
]