from django import forms

Quantity_Choice = [
    (i, str(i)) for i in range(1, 10)
]


class AddCartForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=Quantity_Choice,
        coerce=int,
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )
