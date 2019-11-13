from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.Form):
	author = forms.CharField(max_length=40,widget=forms.TextInput(attrs={"class":"form_control",
					"placeholder":"Enter Name"}))
	reply = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Leave a comment"}))

class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=100)

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args,**kwargs)

		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

	class Meta:
		model = User
		fields = ('username','email','password1','password2')
		
