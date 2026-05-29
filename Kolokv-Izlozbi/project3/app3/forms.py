from django.forms import ModelForm
from .models import *

class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(ExhibitionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'