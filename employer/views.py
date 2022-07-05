from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,View
from candidate.models import company_Profile, jobs,Application
from employer.forms import companyform, addjobform
from django.urls import reverse_lazy
from django.contrib import messages
from employer import forms


# Create your views here.

class companyprofile(CreateView):
    model = company_Profile
    form_class = companyform
    template_name = "add_company_profile.html"

    def post(self, request, *args, **kwargs):
        form = companyform(request.POST, files=request.FILES)
        if form.is_valid():
            Company_logo = form.cleaned_data.get("Company_logo")
            Company_name = form.cleaned_data.get("Company_name")
            Services = form.cleaned_data.get("Services")
            Company_start_date = form.cleaned_data.get("Company_start_date")
            Websites = form.cleaned_data.get("Websites")
            company = company_Profile(Company_logo=Company_logo, Company_name=Company_name, Services=Services,
                                      Company_start_date=Company_start_date, Websites=Websites)
            company.save()
            return redirect("Emphome")
        else:
            return redirect("addcompany")


class Listcompany(ListView):
    model = company_Profile
    context_object_name = "lstcmp"
    template_name = "list_company.html"
    success_url = reverse_lazy("Ehome")
# class Companydetails(DeleteView):
#     model = company_Profile



class addjob(CreateView):
    model = jobs
    form_class = addjobform
    template_name = "add_jobs.html"
    success_url = reverse_lazy("listcompany")



    # def post(self, request, *args, **kwargs):
    #     form = addjobform(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         Job_details = form.cleaned_data.get("Job_details")
    #         Location = form.cleaned_data.get("Location")
    #         Experience = form.cleaned_data.get("Experience")
    #         Salary = form.cleaned_data.get("Salary")
    #
    #         jobsadd = jobs(Job_details=Job_details, Location=Location, Experience=Experience, Salary=Salary)
    #         jobsadd.save()
    #         return redirect("listcompany")
    #     else:
    #         return redirect("addjobs")


class listjob(ListView):
    model = jobs
    template_name = "listjobs.html"
    context_object_name = "lstjb"


class Editjobs(UpdateView):
    model = jobs
    form_class = addjobform
    context_object_name = "editjobs"
    pk_url_kwarg = 'id'
    template_name = "editjobs.html"
    success_url = reverse_lazy("listjobs")

class Jobdelete(DeleteView):
        model = jobs
        pk_url_kwarg = 'id'
        template_name = "delete_jobs.html"
        success_url = reverse_lazy("listjobs")

class Editcompany(UpdateView):
        model = company_Profile
        form_class = companyform
        context_object_name = "editcompany"
        pk_url_kwarg = 'id'
        template_name = "editcompany.html"
        success_url = reverse_lazy("listcompany")


class Companydelete(DeleteView):
    model =company_Profile
    pk_url_kwarg = 'id'
    template_name = "deletecompany.html"
    success_url = reverse_lazy("listcompany")

class Ehome(View):
        def get(self, request, *args, **kwargs):
            return render(request, "Ehome.html")

# class Ownerdashbord(ListView):
#     model =my_application
#     template_name = "applicants.html"
#
#     def get(self, request, *args, **kwargs):
#         newapp = my_application.objects.filter(status="order_placed")
#         context = {"app": newapp}
#         return render(request, "applicants.html", context)
class Applicants(ListView):
    model=Application
    template_name="applicants.html"
    context_object_name = "aform"



