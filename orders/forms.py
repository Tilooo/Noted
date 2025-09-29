# orders/forms.py

from django import forms
from .models import Order

tailwind_input_classes = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': tailwind_input_classes, 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': tailwind_input_classes, 'placeholder': 'Love'}),
            'email': forms.EmailInput(attrs={'class': tailwind_input_classes, 'placeholder': 'you@example.com'}),
            'address': forms.TextInput(attrs={'class': tailwind_input_classes, 'placeholder': '1234 Main St'}),
            'postal_code': forms.TextInput(attrs={'class': tailwind_input_classes, 'placeholder': '10001'}),
            'city': forms.TextInput(attrs={'class': tailwind_input_classes, 'placeholder': 'New York'}),
        }