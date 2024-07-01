from django import forms
from .models import UserDocuments

class UserDocumentForm(forms.ModelForm):
    class Meta:
        model = UserDocuments
        fields = ['title', 'file']