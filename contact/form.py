from django import forms

class Contact_form(forms.Form):
    name=forms.CharField(label="Name", required=True)
    email=forms.CharField(label="Email", required=True)
    content=forms.CharField(label="Content", required=True, widget=forms.Textarea)