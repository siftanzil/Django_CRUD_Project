from django import forms
from first_app import models

class ReciterForm(forms.ModelForm):
    class Meta:
        model = models.Reciter
        fields = '__all__'
        
class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    
    class Meta:
        model = models.Album
        fields = '__all__'