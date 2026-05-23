from django.forms.models import ModelForm
from .models import *

class TravelForm(ModelForm):
    class Meta:
        model = Travel
        exclude = ('guide',)

    def __init__(self, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'