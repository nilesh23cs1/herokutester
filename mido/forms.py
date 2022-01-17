from django import forms
from .models import midomodel

class midoform(forms.ModelForm):
	class Meta:
		model = midomodel                 #defines the model on which i am going to edit
		fields = '__all__'                # and the field i am going to edit