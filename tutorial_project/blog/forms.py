from django import forms

from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth", "bio"]
        exclude = ["created_by", "updated_by", "created_at", "updated_at"]
