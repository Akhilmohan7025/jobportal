from django.urls import path
from candidate import views

urlpatterns = [
    path("accounts/", views.SigninSignout.as_view(), name="select"),
    path("accounts/signup/", views.Sign_up.as_view(), name="signup"),
    path("accounts/signin/", views.Sign_in.as_view(), name="signin"),
    path("add/c_profile/", views.candiateprofileview.as_view(), name="addcandidateprofile"),
    path("candidate/profile/", views.viewmyprofile.as_view(), name="userprofile"),
    path("account/logout", views.signout, name="logout"),
    path("candidate/mainhome/", views.Mainhome.as_view(), name="mainhome"),
    path("candidate/listjobs/", views.Clistjobs.as_view(), name="Cjobs"),
    path("applyform",views.Applicationview.as_view(),name="apform")

]
