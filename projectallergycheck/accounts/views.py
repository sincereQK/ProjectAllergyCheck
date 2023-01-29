from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 
# Create your views here. 
# 회원가입
#장고 내장폼 UserCreationForm 사용
# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
# 			    username=request.POST['username'], 
# 			    password=request.POST['password1'], 
# 			    email=request.POST['email'],
# 		    )
#             auth.login(request, user) 
#             return redirect('/') 
#             return render(request, 'signup.html') 
#     else: 
#         form = UserCreationForm 
#         return render(request, 'signup.html', {'form':form})

# #login부분 컨트롤
# def login_index(request):
#     return render(request,'../templates/login/index.html')

#mypage부분 컨트롤
def accounts_badfood(request):
    return render(request,'templates/accounts/badfood.html')

def accounts_bodyInfo(request):
    return render(request,'templates/accounts/bodyInfo.html')

def accounts_goodfood(request):
    return render(request,'templates/accounts/goodfood.html')

def accounts_mypage(request):
    return render(request,'templates/accounts/mypage.html')

def accounts_nickname(request):
    return render(request,'templates/accounts/nickname.html')

def accounts_warningfood(request):
    return render(request,'templates/accounts/warningfood.html')