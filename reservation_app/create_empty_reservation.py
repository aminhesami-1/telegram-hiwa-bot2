import os
import django
import datetime
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservation_app.settings')
django.setup()

from appointment.models import Appointment

localtz = timezone('Asia/Tehran')
today = datetime.datetime.now()
today = localtz.localize(today)
# print(today)

# use Q to add also month constrain and year
today_appointment = Appointment.objects.filter(check_in__day=today.day)
if len(today_appointment) == 0:
    print('we dont have appointment for today')

    # question = input('do you want me to make some empty appointment objects between 5 to 7 pm? ')
    # if question == 'y':
    check_in_date = datetime.datetime(today.year,today.month,today.day,17)
    check_out_date = datetime.datetime(today.year,today.month,today.day,17,20)

    check_in_date = localtz.localize(check_in_date)
    check_out_date = localtz.localize(check_out_date)
    
    for i in range(6):
        Appointment(check_in=check_in_date ,check_out=check_out_date).save()
        check_in_date += datetime.timedelta(minutes=20)
        check_out_date += datetime.timedelta(minutes=20)
else:
    print('we have some appointment for today')
    for item in today_appointment:
        print(item)
