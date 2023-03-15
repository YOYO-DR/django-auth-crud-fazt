from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    #cascade por si se borra el usuario, se borran sus registros
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
      return self.title+" - del usuario "+self.user.username
    #minuto 1:19:00