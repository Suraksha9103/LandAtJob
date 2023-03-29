from django.urls import path
from .import views


urlpatterns = [
    path('JobSeekerlogin/',views.loginForm, name="JobSeeker.login"),
    path('JobSeekersignup/',views.SignUpForm,name="JobSeeker.signup"),
     
]