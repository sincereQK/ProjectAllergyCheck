from django.shortcuts import render

# Create your views here.
def index(request):
    #context = {'msg':'hello','name':'Matt'}
    return render(request,'../templates/index.html')

