from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
from django.contrib.auth.models import User


def create_user(username, password):
    user = User(username=username, password=password)
    user.save()


# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
        
#         # Ensure that username is not empty
#         if username:
#             user = User.objects.create_user(username=username, password=password, email=email)
#             user.save()
#             # Perform additional actions or redirect as needed
#         else:
#             # Handle case where username is empty
#             pass

    # Handle GET request or other logic


# Create your views here.
from django.contrib.auth.models import User

def register(request):
    
    username = request.POST.get('username')
    password=request.POST.get('password')
    new_user = User(username=username)
    
    new_user.set_password('password')  
    new_user.email = 'user@example.com'  

    
    new_user.save()

    
    return HttpResponse('User registered successfully.')


# def register(request):
#     if request.method=="POST":
#         form=MyForm(request.POST)
#         username=request.POST.get('username')
#         password=request.POST.get('password')


        # if User.objects.filter(username=username).exists():
        #     print('helloo')
        #     # messages.warning(request,'user already exist')
        #     return redirect('register')     
        # else:
        #     obj=User()
        #     obj.username=username
        #     obj.set_password(password)
        #     obj.save()
        #     id=User.objects.get(username=username).id
        #     Client.objects.create(username=username,password=password,id=id)
            
        
        #     # form=LoginForm()
        #     # return render(request,'Login.html',{'form':form})
        #     return redirect('signin')
            
         
    # else:
    #     form=MyForm()
    #     return render(request,'register.html',{'form':form})

    
           
          