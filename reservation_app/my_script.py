import os
import django
from django.core.exceptions import ObjectDoesNotExist
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reservation_app.settings")
django.setup()
from basic_user.models import Basic_User
from questions.models import Question
from asgiref.sync import sync_to_async
import requests
import json

url = "https://api2.ippanel.com/api/v1/sms/pattern/normal/send"
headers = {
    "apikey": "F4nixrUXZG99qaDnMiqvG5Oyl5zlzYo8_8j1Vy5XZ3M=",
    "Content-Type": "application/json",
}


async def set_user_id(user_id):
    new_user = Basic_User(User_Id=user_id)
    await sync_to_async(new_user.save)()


async def set_user_name(user_id, name):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    user.name = name
    await sync_to_async(user.save)()


async def set_user_age(user_id, age):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    user.age = age
    await sync_to_async(user.save)()


async def set_user_number(user_id, number):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    user.number = number
    await sync_to_async(user.save)()


async def show_user_data(user_id):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    return [user.name, user.age, user.number]


async def delete_user_data(user_id):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    await sync_to_async(user.delete)()


async def V_code(user_id, v_code):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    user.v_code = v_code
    await sync_to_async(user.save)()
    payload = json.dumps(
        {
            "code": "49t54yg3lichqyb",
            "sender": "+983000505",
            "recipient": f"{user.number}",
            "variable": {"verification_code": v_code},
        }
    )
    requests.request("POST", url, headers=headers, data=payload)


async def is_user_verify(user_id):
        try :
             user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
        except Basic_User.DoesNotExist :
            return False
        if user.is_user_verifyed :
         return True
        else :
            return False

async def is_user_id_set(user_id):
    try:
        user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
        return True
    except Basic_User.DoesNotExist:
        return False

async def check_v_code(user_id , user_v_code):
    user = await sync_to_async(Basic_User.objects.get)(User_Id=user_id)
    if user.v_code == user_v_code :
        user.is_user_verifyed = True
        await sync_to_async(user.save)()
        return True
    else :
        return False



async def get_questions():
    question = await sync_to_async(Question.objects.all)()
    question_dict = {}
    for item in question :
        question_dict['q'+str(item.id)] = [item.text,item.answer]  

    return question_dict
    
