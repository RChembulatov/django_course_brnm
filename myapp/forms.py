from django import forms
from .models import Contact, Product, Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class ReviewForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all().order_by('name'), label="Выберите продукт", empty_label="Выберите продукт")

    class Meta:
        model = Review
        fields = ['product', 'author', 'text']
