from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth import login ,authenticate
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task(title=title)
        task.save()
        return HttpResponseRedirect('/')

    context = {"tasks":tasks}
    return render(request,'index.html',context)




@login_required
def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect('/')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('/')
        else:
            return redirect("login/")
    return render(request,'login.html')

@login_required
def Logout(request):
    dj_logout(request)
    return redirect('/login/')