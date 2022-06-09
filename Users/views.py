from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm, UserForm,AdminloginForm
from django.contrib.auth import authenticate,login

# Create your views here.
app_name = 'Users'
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Welcome { username }')
            return HttpResponseRedirect('/users/')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def addnew(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = UserForm()  
    return render(request,'users/index.html',{'form':form})

def user_index(request):  
    users = User.objects.all()  
    return render(request,"users/show.html",{'users':users})

def edit(request, id):  
    user = User.objects.get(id=id)  
    return render(request,'users/edit.html', {'user':user})

def update(request, id):  
    user = User.objects.get(id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, 'users/edit.html', {'user': user})

def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    return HttpResponseRedirect('/users/')

@staff_member_required
def Adminlogin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/usermaster/')
    if request.method=='GET':
        form=AdminloginForm(request.POST)
        if form.is_valid():

            user=authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password'])
            if user:
                print('user',user)
                login(request,user)
                return redirect('/usermaster/')
            else:
                print('Not authenticated')
    elif request.method=='GET':
        if request.user.is_authenticated:
            return redirect('/usermaster/')
        form=AdminloginForm()
    return render(request,'users/adminlogin.html',{'form':form})