from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
