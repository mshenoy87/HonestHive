from django import forms

from Waggles.models import Waggle

MAX_WAGGLE_LENGTH = 240

class WaggleForm(forms.ModelForm):
    class Meta:
        model = Waggle
        fields = ["waggleText"]

    def clean_content(self):
        content = self.cleaned_data.get("waggleText")
        if (len(content) > MAX_WAGGLE_LENGTH):
            raise forms.ValidationError("This waggle is too long!")
        return content
