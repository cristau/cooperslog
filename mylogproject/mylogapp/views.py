import pandas as pd
import requests

from django.shortcuts import render
from datetime import datetime
# from django.http import HttpResponse


api_key = "0d68497c794f4b545178c4de73d82453"
city_name = "New York"
state_code = "NY"
country_code = "US"
units = "imperial"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&units={units}&appid={api_key}"
response = requests.get(url)

def log_page(request):
    return render(request, 'mylogapp/index.html', {})

def submit_activity(request):
    print('youve loaded the activity page')

    return render(request, 'mylogapp/activity_form.html', {})

def success(request):
    if request.method == 'POST':
        fields = {}
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            elif value == '':
                fields[key] = None
            else:
                fields[key] = value

    start_time = datetime.strptime(fields['start_time'], '%Y-%m-%dT%H:%M')
    end_time = datetime.strptime(fields['end_time'], '%Y-%m-%dT%H:%M')

    fields['duration'] = (end_time - start_time)

    if response.status_code == 200:
        data = response.json()
    
        # You can access various weather data from the 'data' dictionary
        # For example, to get the temperature:
        data_main = data['main']
    
        print(f"data: {data_main}")
    
    # You can access other weather information in a similar way
    else:
        print("Error: Unable to retrieve weather data")

    df = pd.DataFrame(fields, index=[0])
    print(df)

    print(fields)
    return render(request, 'mylogapp/success.html', {})