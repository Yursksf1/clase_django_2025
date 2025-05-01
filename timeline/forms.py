from django import forms
from .models import TimeLine

class TimeLineForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        fields = ['year', 'name', 'description']

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 1900:
            raise forms.ValidationError("El año debe ser mayor a 1900.")
        return year