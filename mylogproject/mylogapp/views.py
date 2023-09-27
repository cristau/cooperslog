from django.shortcuts import render
# from django.http import HttpResponse

def log_page(request):
    return render(request, 'mylogapp/index.html', {})

def submit_activity(request):
    return render(request, 'mylogapp/activity_form.html', {})