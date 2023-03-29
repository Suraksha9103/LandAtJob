
from django.urls import path
from .import views


urlpatterns = [

    path('',views.index, name="index"),
    path('login/',views.loginForm, name="login"),
    path('signup/',views.SignUpForm,name="signup"),
     
    


    path('list/', views.jobList, name='job.list'),
    path('store', views.jobStore,name='job.store'),
    path('add', views.createJob,name='job.create'),
    path('edit/<int:id>', views.jobEdit,name='job.edit'),
    path('delete/<int:id>', views.jobDelete,name='job.delete'),
    path('update/<int:id>', views.jobUpdate,name='job.update'),


 ] 