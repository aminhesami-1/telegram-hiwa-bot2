from django.db import models

# Create your models here.
class Basic_User(models.Model):
    User_Id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128, blank=True)
    age= models.CharField(max_length=3 ,blank=True)
    number = models.CharField(max_length=128,blank=True )
    v_code = models.CharField(max_length=6 , blank=True)
    is_user_verifyed = models.BooleanField(default=False)
   
    



    def __str__(self) -> str:
        return f'{self.User_Id}: {self.name}'
