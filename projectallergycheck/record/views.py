from django.shortcuts import render

# Create your views here.
# record 부분 컨트롤
def record_all_scan_list(request):
    return render(request,'templates/record/all-scan-list.html')

def record_latest_scan_list(request):
    return render(request,'templates/record/latest-scan-list.html')