from django.shortcuts import render,redirect
from jobs.models import Job,JobRequests

# Create your views here.

from website.forms import RegistrationForm


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,get_user_model

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


@login_required
def logged_in(request):
    jobs =Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request,"logged_in.html",context)