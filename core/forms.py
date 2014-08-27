from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("name", "description", "category")

    def save(self, user, commit=True):
        m = super(BoardForm, self).save(commit=False)
        m.user = user
        if commit:
            m.save()
        return m



