from django import forms
from django.forms import ModelForm
from candidate.models import company_Profile,jobs,Application


class companyform(forms.ModelForm):
    class Meta:
        model =company_Profile
        exclude=("user",)

        widgets = {

            "Company_logo": forms.FileInput(attrs={"class": "form-control"}),
            "Company_name": forms.TextInput(attrs={"class": "form-control"}),
            "Services": forms.TextInput(attrs={"class": "form-control"}),
            "Company_start_date": forms.DateInput(attrs={"class": "form-control"}),
            "Websites":  forms.URLInput(attrs={"class": "form-control"}),

        }
class addjobform(forms.ModelForm):
    class Meta:
        model=jobs
        fields="__all__"

        widgets = {
            "Job_details": forms.Textarea(attrs={"class": "form-control"}),
            "Location": forms.TextInput(attrs={"class": "form-control"}),
            "Experience": forms.NumberInput(attrs={"class": "form-control"}),
            "Salary": forms.TextInput(attrs={"class": "form-control"}),
            "Skills": forms.TextInput(attrs={"class": "form-control"}),
        }
