from django.urls import path
from employer import views

urlpatterns = [
    path("addprofile", views.companyprofile.as_view(), name="addcompany"),
    path("mainhome/", views.Ehome.as_view(), name="Emphome"),
    path("listcompanies", views.Listcompany.as_view(), name="listcompany"),
    path("editcompany/<int:id>", views.Editcompany.as_view(), name="editcompany"),
    path("company/del/<int:id>", views.Companydelete.as_view(), name="deletecompany"),
    path("addjobs", views.addjob.as_view(), name="addjobs"),
    path("listjobs", views.listjob.as_view(), name="listjobs"),
    path("edit/<int:id>", views.Editjobs.as_view(), name="editjobs"),
    path("jobs/del/<int:id>", views.Jobdelete.as_view(), name="deletejobs"),
    path("emp/Applicants/", views.Applicants.as_view(), name="Applicants"),
]
