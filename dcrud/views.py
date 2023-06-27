from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,Add_recordForm
from .models import Record

def home(request):
    records=Record.objects.all() 
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In Successfully")
            return redirect('home')
        else:
            messages.success(request,' There was an error logging in Try again Later')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})



def login_user(request):
    pass



def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out.....")
    return redirect('home')


def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"You have succesfully Registered")
            return redirect('home')
    else:
        form =SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def data_record(request,pk):
    if request.user.is_authenticated:
        data_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'data_record':data_record})
    else:
        messages.success(request,"Login in to view the records")
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Succesffully deleted")
        return redirect('home')
    else:
        messages.success(request,"Login in to delete the records")
        return redirect('home')



def add_record(request):
    form =Add_recordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Succesfully Added")
                return redirect('home')    
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You Must Login first")
        return redirect('home')
    


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form =Add_recordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You Must Login first")
        return redirect('home')





