from django import forms
from .models import Address


class OrderForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_user', 'city', 'country', 'postal_code']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control input-sm'
            self.fields['address_user'].label = 'Address'
