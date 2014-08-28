from django import forms

from .models import Board, Pin

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


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ("board", "description", "image")

    def save(self, user, commit=True):
        m = super(PinForm, self).save(commit=False)
        m.created_by = user
        if commit:
            m.save()
        return m



