from django import forms
from .models import Orders
from cart.models import CartItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['address', 'city', 'country', 'postal_code']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control input-sm'
            self.fields['address'].label = 'Address'
