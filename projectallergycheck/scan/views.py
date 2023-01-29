from django.shortcuts import render

# Create your views here.
# scan 부분 컨트롤
def scan_scan_list(request):
    return render(request,'templates/scan/scan-list.html')