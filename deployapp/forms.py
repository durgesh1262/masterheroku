from django import forms 
from .models import DeployModel

class DeployHerokoForm(forms.ModelForm):
    class Meta():
        model = DeployModel
        fields = '__all__'
        