from django import forms
from .models import policeuser

class policelogin(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    def clean(self):
        cleanuser = self.cleaned_data['user']
        cleanpass = self.cleaned_data['password']
        try:
            p = policeuser.objects.get(user=cleanuser, password=cleanpass)
        except policeuser.DoesNotExist:
            raise forms.ValidationError("No such police user")
