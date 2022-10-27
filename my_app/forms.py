from django import forms


class CarForm(forms.Form):
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "car-brand",
                "placeholder": "marca del coche",
                "required": "True",
            }
        ),
    )
    model = forms.IntegerField(
        label="Modelo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "car-model",
                "placeholder": "modelo",
                "required": "True",
            }
        ),
    )
