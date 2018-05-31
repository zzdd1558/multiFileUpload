from .models import UploadFileModel
from django import forms

class UploadFileForm(forms.ModelForm):
    class Meta : 
        model = UploadFileModel
        fields = ['file']


