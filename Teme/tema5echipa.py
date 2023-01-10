# 1
from datetime import datetime
import datetime
import pytz
def data_si_ora():
    data_si_ora = datetime.datetime.now()
    print(data_si_ora)

data_si_ora()

x = pytz.timezone('Asia/Hong_Kong')

print(datetime.datetime.now(tz=x))

# varianta 2
def current_date_time(country):
    if country == 'Romania':
        current_time = datetime.datetime.now(pytz.timezone('Europe/Bucharest'))
        print(f"The current time in {country} is:")
        print(f"Date: {current_time.year}-{current_time.month}-{current_time.day}")
        print(f"Hour: {current_time.hour}:{current_time.minute}:{current_time.second}")
    if country == 'China':
        current_time = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong'))
        print(f"The current time in {country} is:")
        print(f"Date: {current_time.year}-{current_time.month}-{current_time.day}")
        print(f"Hour: {current_time.hour}:{current_time.minute}:{current_time.second}")


current_date_time('Romania')
current_date_time('China')

"""
2. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

def get_days_until_christmas():
    today = datetime.date.today()
    future = datetime.date(2022, 12, 25)
    diff = future - today
    print(f'Pana la Crăciun mai sunt: {diff.days} de zile')


get_days_until_christmas()

# varianta 2 zi nastere

def get_days_until_birthday():
    today = datetime.date.today()
    future = datetime.date(2023, 5, 13)
    diff = future - today
    print(f'Pana la ziua mea mai sunt: {diff.days} de zile')


get_days_until_birthday()