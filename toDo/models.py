from django.db import models
from django.contrib.auth.models import User
#automatyczny model Usera w Django, nie trzeba dodawać go jako klasy, chyba że chcemy usera modyfikować =
# = jeśli chcemy by user logowł się przez email lub dodać jakieś pole itd.

# tytul
# opis(opcjonalny)
# wazne(lub nie)
# data utworzenia (ktora ma sie dodawac automatycznie)
# data zakonczenia (dodawane recznie)
# polacznie z userem

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    importance = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(blank=True, null=True)#większość pól z wyjątkiem charfield i textfield wymagają blank i null = True
    user = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE = wpis zniknie, jeśli usuniemy usera


