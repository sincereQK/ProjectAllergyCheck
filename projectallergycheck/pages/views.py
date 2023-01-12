from django.shortcuts import render

# Create your views here.

#여기가 controller
#시작페이지
def index(request):
    #테스트용
    #context = {'msg':'hello','name':'Matt'}
    return render(request,'../templates/index.html')

#about부분 컨트롤
def about_edit(request):
    return render(request,'../templates/about/edit.html')

def about_home(request):
    return render(request,'../templates/about/home.html')

def about_list(request):
    return render(request,'../templates/about/list.html')

def about_qrcode(request):
    return render(request,'../templates/about/qrCode.html')

def about_test(request):
    return render(request,'../templates/about/test.html')

def about_user(request):
    return render(request,'../templates/about/user.html')


#login부분 컨트롤
def login_index(request):
    return render(request,'../templates/login/index.html')


#mypage부분 컨트롤
def mypage_badfood(request):
    return render(request,'../templates/mypage/badfood.html')

def mypage_bodyInfo(request):
    return render(request,'../templates/mypage/bodyInfo.html')

def mypage_goodfood(request):
    return render(request,'../templates/mypage/goodfood.html')

def mypage_mypage(request):
    return render(request,'../templates/mypage/mypage.html')

def mypage_nickname(request):
    return render(request,'../templates/mypage/nickname.html')

def mypage_warningfood(request):
    return render(request,'../templates/mypage/warningfood.html')


#recommend부분 컨트롤
def recommend_all_recommend_list(request):
    return render(request,'../templates/recommend/all_recommend_list.html')

def recommend_nutrient_recommend(request):
    return render(request,'../templates/recommend/nutrient_recommend.html')

def recommend_user_recommend(request):
    return render(request,'../templates/recommend/user_recommend.html')



#scan부분 컨트롤
def scan_all_scan_list(request):
    return render(request,'../templates/scan/all-scan-list.html')


