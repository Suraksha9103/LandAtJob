from .models import AddJob

def recruiterStore(request):
    job=AddJob(
        user_id                 =request.user.id,
        title=request.POST['title'],
        description=request.POST['description'],
        location=request.POST['location'],
        type=request.POST['type'],
        category=request.POST['category'],
        last_date=request.POST['last_date'],
        company_name=request.POST['company_name'],
        website=request.POST['website'],
        job_photo               =request.FILES.get('job_photo',False),                 
        created_at              =request.POST.get('created_at',False),
        updated_at              =request.POST.get('updated_at',False),
        
    )
    job.save()
    return "sucess"


def updatejob(request,id):
    job=AddJob.objects.get(id=id)
    job.title = request.POST["title"]
    job.description=request.POST["description"]
    job.location= request.POST['location']
    job.type=request.POST['type']
    job.category=request.POST['category']
    job.last_date=request.POST['last_date']
    job.company_name=request.POST[' company_name']
    job.website=request.POST['website']
    job.job_photo                   =request.FILES.get('job_photo',False)
    job.created_at              =request.POST.get('created_at',False)
    job.updated_at              =request.POST.get('updated_at',False)
    job.save()
    return "sucess"

def deletejob(id):
    job = AddJob.objects.get(id = id)
    job.delete()
    return "success"

def getjobId(id):
    job = AddJob.objects.get(id= id)
    return job

def getjob():
    job =  AddJob.objects.values().all()
    return list(job)