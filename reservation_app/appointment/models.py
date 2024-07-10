from django.db import models
from basic_user.models import Basic_User
import datetime

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(Basic_User, on_delete=models.CASCADE,null=True, blank=True)
    check_in = models.DateTimeField(null=True,blank=True)
    check_out = models.DateTimeField(null=True,blank=True)
    reserved = models.BooleanField(default=False, blank=True, null=True)


    def reservation_expired(self):
        now = datetime.datetime.now(tz=datetime.timezone(offset=datetime.timedelta()))
        if self.check_out < now:
            return True
        else:
            return False
        
    def today_available_reservations(self):
        today = datetime.date.today() 
        today_reservation = Appointment.objects.filter(time__date=today,reserved=False)
        return today_reservation
    
    def __str__(self) -> str:
        return f"No.{self.id} from {self.check_in.hour}:{self.check_in.minute} to {self.check_out.hour}:{self.check_out.minute}"
    

    def create_empty_reservation():
        # * * * * * /usr/bin/python3  /home/<path to the creator file>
        pass
