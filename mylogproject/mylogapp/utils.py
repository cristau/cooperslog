import pandas as pd
from datetime import datetime

format_string = "%Y-%m-%d %H:%M:%S"

df = pd.read_csv('cooperslog.csv')

# day_one = {
#     'activity_id': [0,1],
#     'activity': ['Ice Bath', 'Ab Workout'],
#     'details': ['55 degrees fahrenheit', 'Perfomed 8 different ab exercises'],
#     'start_time': [datetime.strptime('2023-09-24 08:02:15', format_string), datetime.strptime('2023-09-24 08:22:57', format_string)], 
#     'end_time': [datetime.strptime('2023-09-24 08:07:23', format_string), datetime.strptime('2023-09-24 08:51:11', format_string)],
#     'duration': [datetime.strptime('2023-09-24 08:07:23', format_string) - datetime.strptime('2023-09-24 08:02:15', format_string), datetime.strptime('2023-09-24 08:51:11', format_string) - datetime.strptime('2023-09-24 08:22:57', format_string)],
#     'suck_score': [3, 4],
#     'category': ['Recovery', 'Workout'],
#     'body_score': [60, 60],
#     'aches': ['achilles tendinitis', 'achilles tendinitis'],
#     'injuries': [None, None]
# }

# activity_id = input('Activity ID: ')
activity = input('Activity: ')
details = input('Details: ')
start_time = input('Start Time (yyyy-mm-dd hh:mm:ss): ')
end_time = input('End Time (yyyy-mm-dd hh:mm:ss): ')
duration = datetime.strptime(end_time, format_string) - datetime.strptime(start_time, format_string)
suck_score = input('Suck Score (1-10): ')
category = input('Category (Recovery, Workout, etc): ')
body_score = input('Body Score (1-100): ')
aches = input('Aches: ')
injuries = input('Injuries: ')

new_log = {
    'activity_id': len(df.index), 
    'activity': activity, 
    'details': details, 
    'start_time': start_time, 
    'end_time': end_time, 
    'duration': duration, 
    'suck_score': suck_score, 
    'category': category, 
    'body_score': body_score, 
    'aches': aches, 
    'injuries': injuries
}

confirmation_msg = input('Everything look good? (Y/N): ')

while confirmation_msg == 'N':
    print('')
    print('Starting over with current entry...')
    print('')

    activity = input('Activity: ')
    details = input('Details: ')
    start_time = input('Start Time (yyyy-mm-dd hh:mm:ss): ')
    end_time = input('End Time (yyyy-mm-dd hh:mm:ss): ')
    duration = datetime.strptime(end_time, format_string) - datetime.strptime(start_time, format_string)
    suck_score = input('Suck Score (1-10): ')
    category = input('Category (Recovery, Workout, etc): ')
    body_score = input('Body Score (1-100): ')
    aches = input('Aches: ')
    injuries = input('Injuries: ')

    confirmation_msg = input('Everything look good? (Y/N): ')

    new_log = {
        'activity_id': len(df.index), 
        'activity': activity, 
        'details': details, 
        'start_time': start_time, 
        'end_time': end_time, 
        'duration': duration, 
        'suck_score': suck_score, 
        'category': category, 
        'body_score': body_score, 
        'aches': aches, 
        'injuries': injuries
    }

new_log_df = pd.DataFrame([new_log])
df = pd.concat([df, new_log_df], ignore_index=True)

print('')
print('Activity logged!')
print('')

response = input('Would you like to input another activity (Y/N)?: ')

while response == 'Y':
    activity = input('Activity: ')
    details = input('Details: ')
    start_time = input('Start Time (yyyy-mm-dd hh:mm:ss): ')
    end_time = input('End Time (yyyy-mm-dd hh:mm:ss): ')
    duration = datetime.strptime(end_time, format_string) - datetime.strptime(start_time, format_string)
    suck_score = input('Suck Score (1-10): ')
    category = input('Category (Recovery, Workout, etc): ')
    body_score = input('Body Score (1-100): ')
    aches = input('Aches: ')
    injuries = input('Injuries: ')

    new_log_df = pd.DataFrame([new_log])
    df = pd.concat([df, new_log_df], ignore_index=True)

    print('')
    print('Activity logged!')
    print('')

    df.to_csv('cooperslog.csv', mode='w', header=True, index=False)
    
    response = input('Would you like to input another activity (Y/N)?: ')
    if response == 'Y':
        print('')
        print('Enter another activity: ')
        print('')
    elif response == 'N':

        print('')
        print('Iterum surgo.')
        print('')
        exit()
# if 'activity' in day_one:
#     day_one['activity'].append()


# df = pd.DataFrame.from_dict(day_one, orient='index')
# df = df.transpose()
print(df.head())
# df.to_csv('cooperslog.csv', mode='w', header=True, index=False)