from django.shortcuts import render,redirect,get_object_or_404
from jobs.models import Job,JobRequests
from django.contrib import messages

# Create your views here.

from website.forms import RegistrationForm

from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.urls import reverse
def homepage(request):
     return render(request,"homepage.html")



def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()

        context = {'form':form}

        return render(request,"register.html",context)

## this function lists the avaliable jobs after user getting logged in
@login_required
def logged_in(request):
    jobs =Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request,"logged_in.html",context)



def job_detail(request,id = None):
    job_instance = get_object_or_404(Job,job_id=id)
    context = {
        'job':job_instance
    }

    r =  request.GET.get('request')
    if r:
        if request.user.is_authenticated:
            if r == 'yes':
                #add this user to request model
                if not JobRequests.objects.filter(request_by= request.user, request_on = job_instance ).exists():
                    job_request = JobRequests.objects.create(
                        request_by = request.user,
                        request_on = job_instance
                    )
                    messages.success(request,"request sent successfully")
                    return HttpResponseRedirect(reverse('job_detail',kwargs={
                        'id':job_instance.job_id

                    }))
                else:
                    messages.info( request,"job already applied")
                    return HttpResponseRedirect(reverse('job_detail',kwargs={'id':job_instance.job_id}))

            else: # ask him to login
                return HttpResponseRedirect(reverse('login-page'))

    return  render(request,"job_detail.html",context)








