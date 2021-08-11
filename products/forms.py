from django import forms


class ContactForm(forms.Form):
	email = forms.EmailField(required=True)
	subject= forms.CharField(max_length=100,required=True)
	message=forms.CharField(widget=forms.Textarea,max_length=500,required=True)


