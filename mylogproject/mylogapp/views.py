from django.shortcuts import render
# from django.http import HttpResponse

def log_page(request):
    return render(request, 'mylogapp/index.html', {})

def submit_activity(request):
    print('youve loaded the activity page')

    return render(request, 'mylogapp/activity_form.html', {})

def success(request):
    if request.method == 'POST':
    # Access all form inputs in request.POST
        for key, value in request.POST.items():
            print(key, value)
    return render(request, 'mylogapp/success.html', {})