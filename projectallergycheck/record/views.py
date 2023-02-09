from django.shortcuts import render

# Create your views here.
# record 부분 컨트롤
def record_all_scan_list(request):
    return render(request,'./record/all-scan-list.html')

def record_latest_scan_list(request):
    return render(request,'./record/latest-scan-list.html')

def record_scan_list(request):
    return render(request,'./record/scan-list.html')