import pandas as pd
from datetime import datetime

from garmin import garmin

daily_activities = garmin.get_activities_fordate('2023-11-09')

print(daily_activities['ActivitiesForDay']['payload'])
