from django.shortcuts import render

# Create your views here.

#여기가 controller
#시작페이지
def index(request):
    #테스트용
    #context = {'msg':'hello','name':'Matt'}
    return render(request,'./index.html')

# #about부분 컨트롤
def about_qrcode(request):
    return render(request,'./pages/about/qrCode.html')

def about_test(request):
    return render(request,'./pages/about/test.html')

def about_user(request):
    return render(request,'./pages/about/user.html')

#recommend부분 컨트롤
def recommend_all_recommend_list(request):
    return render(request,'./pages/recommend/all_recommend_list.html')

def recommend_nutrient_recommend(request):
    return render(request,'./pages/recommend/nutrient_recommend.html')

def recommend_user_recommend(request):
    return render(request,'./pages/recommend/user_recommend.html')