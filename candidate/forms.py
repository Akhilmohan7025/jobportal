from django import forms
from django.forms import ModelForm
from candidate.models import MyUser
from candidate.models import Candidateprofile,Application
from django.contrib.auth.forms import UserCreationForm


class candidateform(forms.ModelForm):
    class Meta:
        model =Candidateprofile
        fields = "__all__"

        widgets = {

            "photo": forms.FileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control"}),
            "email":  forms.EmailInput(attrs={"class": "form-control"}),
            "resume": forms.FileInput(attrs={"class": "form-control"}),

        }

class Applicationform(forms.ModelForm):
    class Meta:
        model=Application
        fields = "__all__"

        widgets = {

            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control"}),
            "country":  forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "grad_year": forms.DateInput(attrs={"class": "form-control"}),
            "postion_for_which_you_applying": forms.TextInput(attrs={"class": "form-control"}),
            "resume": forms.FileInput(attrs={"class": "form-control"}),

        }

class UsersignupForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'role', 'phone']
        widget={
            'date_of_birth':forms.DateInput(attrs={"class":"form-control"}),
            'role': forms.Select(attrs={"class": "form-control"}),
            'phone-no': forms.NumberInput(attrs={"class": "form-control"}),


        }


class userloginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class Profileform(forms.ModelForm):
    class Meta:
        model = Candidateprofile
        fields = ["photo", "name", "dob","mobile", "email", "resume"]
        widgets = {
            'photo': forms.TextInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'dob': forms.DateInput(attrs={"class": "form-control"}),
            'mobile': forms.NumberInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'resume': forms.FileInput(attrs={"class": "form-control"})
        }



