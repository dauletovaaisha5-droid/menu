from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название блюда', 'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'Калории', 'class': 'form-control', 'min': 0}),
        }
