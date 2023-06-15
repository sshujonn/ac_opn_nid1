from django import forms
from django.forms import TextInput

from remit.models import CustomCustomer


class CustomCustomerForm(forms.ModelForm):

    class Meta:
        model = CustomCustomer
        fields = '__all__'
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='dd-mm-yyyy')
        }

    def __init__(self, *args, **kwargs):
        super(CustomCustomerForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.items():
            if k != 'dob':
                v.widget = TextInput(attrs={'class': 'form-control'})