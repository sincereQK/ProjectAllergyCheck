from django.shortcuts import render

# Create your views here.

#여기가 controller
#시작페이지
def index(request):
    #테스트용
    #context = {'msg':'hello','name':'Matt'}
    return render(request,'../templates/index.html')

#about부분 컨트롤
def aboutEdit(request):
    return render(request,'../templates/about/Edit.html')

def aboutHome(request):
    return render(request,'../templates/about/Home.html')

def aboutList(request):
    return render(request,'../templates/about/List.html')

def aboutQRcode(request):
    return render(request,'../templates/about/qrCode.html')

def aboutTest(request):
    return render(request,'../templates/about/Test.html')

def aboutUser(request):
    return render(request,'../templates/about/User.html')

#login부분 컨트롤


#mypage부분 컨트롤


#recommend부분 컨트롤


#scan부분 컨트롤

