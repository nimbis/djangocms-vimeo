from django import forms
from .models import VimeoVideo


class VimeoVideoForm(forms.ModelForm):
    class Meta:
        model = VimeoVideo
        exclude = ('page', 'position', 'placeholder', 'language',
                   'plugin_type')