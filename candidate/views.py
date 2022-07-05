from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView, TemplateView,DetailView
from candidate.models import Candidateprofile, jobs, Application, MyUser
from candidate import forms
from candidate.forms import candidateform, Applicationform,Profileform
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse_lazy


class candiateprofileview(CreateView):
    model = Candidateprofile
    form_class = candidateform
    template_name = "add_candidate_profile.html"

    def post(self, request, *args, **kwargs):
        form = candidateform(request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.cleaned_data.get("photo")
            name = form.cleaned_data.get("name")
            dob = form.cleaned_data.get("dob")
            mobile = form.cleaned_data.get("mobile")
            email = form.cleaned_data.get("email")
            resume = form.cleaned_data.get("resume")
            userp = Candidateprofile(photo=photo, name=name, dob=dob, mobile=mobile, email=email, resume=resume)
            userp.save()
            return redirect("mainhome")
        else:
            return redirect("addcandidateprofile")



class viewmyprofile(TemplateView):
    model = Profileform
    template_name = "userprofile.html"
    form_class = Profileform


class Mainhome(View):
    def get(self, request, *args, **kwargs):
        home = jobs.objects.all()
        context = {"home": home}
        return render(request, "mainhome.html", context)


class Clistjobs(ListView):
    model=jobs
    template_name="Clistjobs.html"
    context_object_name = "home"


class Applicationview(CreateView):
    model = Application
    form_class = Applicationform
    template_name = "Applicationform.html"

    def post(self, request, *args, **kwargs):
        form = Applicationform(request.POST, files=request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            address = form.cleaned_data.get("address")
            phone_number = form.cleaned_data.get("phone_number")
            location = form.cleaned_data.get("location")
            grad_year = form.cleaned_data.get("grad_year")
            postion_for_which_you_applying = form.cleaned_data.get("postion_for_which_you_applying")
            resume = form.cleaned_data.get("resume")
            user = Application(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, location=location,grad_year=grad_year, postion_for_which_you_applying=postion_for_which_you_applying, resume=resume)
            user.save()
            return redirect("mainhome")
        else:

            return redirect("apform")


class Sign_up(CreateView):
    template_name = "Signup.html"
    form_class = forms.UsersignupForm
    success_url = reverse_lazy("signin")
    model = MyUser


class Sign_in(TemplateView):
    template_name = "Sign_in.html"

    def get(self, request):
        form = forms.userloginform()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        log = forms.userloginform(request.POST)
        if log.is_valid():
            email = log.cleaned_data.get("email")
            password = log.cleaned_data.get("password")

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                if request.user.is_admin:
                    return redirect("Emphome")
                else:
                    return redirect("mainhome")




def signout(request):
    logout(request)
    return redirect("signin")

class SigninSignout(TemplateView):
    template_name = "signin_out.html"




