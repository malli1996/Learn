from django import forms
from deployment.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
