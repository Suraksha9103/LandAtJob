from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from JobProvider import service
from .models import AddJob



def index(request):
    return render(request,'JobProvider/index.html')

# Create Login For Job Provider
def SignUpForm(request):
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        if password1 != password2:
            #messages.success(request, 'first password and second password is not correct!!!')
            return HttpResponse("Your password and confrom password doesnot match !!!")
        if User.objects.filter(username=username).first():
            #messages.success(request, "Such a user has already registered!!!")
            return HttpResponse('Such a user has already registered!!!')

        if User.objects.filter(email=email).first():
            #messages.success(request, "This email has already been registered!!!")
            return HttpResponse('This email has already been registered!!!')
        user_obj = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user_obj.set_password(raw_password=password1)
        user_obj.save()
        return redirect('index')

    return render (request,'JobProvider/signup.html')


#  #Create login for Job provider
def loginForm(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('job.create')
        else:
            messages.success(request, "This email has already been registered!!!")
            # return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'JobProvider/login.html')

def createJob(request):
    data={
        'title':"job"
    }
    return render(request,'JobProvider/postjob.html',data)

# # Saving Data to Database extracted from Template

def jobStore(request):
   # print(request.POST)
    store= service.recruiterStore(request)
    return redirect('job.list')

# Showing data from database in template
def jobList(request):
    job=AddJob.objects.all()
    data={
        'job':job
    }
    return render(request,'JobProvider/list.html',data)

#Create the edit form
def jobEdit(request,id):
    job=service.getVechalId(id)
    data={
        'title':'product',
        'driver':service.getjobId(id),
        'job':job
    }
    return render(request,'JobProvider/postjob.html',data)

#update the data in database and template
def jobUpdate(request,id):
    service.updatejob(request, id)
    return redirect('job.list')

#deletion
def jobDelete(request,id):
    service.deletejob(id)
    return redirect('job.list')
















