import os
import django
import datetime

from pytz import timezone
from asgiref.sync import sync_to_async
import asyncio
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservation_app.settings')
django.setup()
from appointment.models import Appointment
from basic_user.models import Basic_User
localtz = timezone('Asia/Tehran')

today = datetime.datetime.now()
today = localtz.localize(today)


async def show_r_data():
    all = await sync_to_async(Appointment.objects.filter)(check_in__day=today.day, reserved=0)
    return all





async def set_reservation_time(user_id , r_data):
    User = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    set_appointment = await sync_to_async(Appointment.objects.get)(id=r_data)
    set_appointment.user = User
    set_appointment.reserved = True
    await sync_to_async(set_appointment.save)()

    
async def check_user_reservation_time(user_id):
    User = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    all = User.appointment_set.all()
    if all != None :
        return True
    else :
        return False



