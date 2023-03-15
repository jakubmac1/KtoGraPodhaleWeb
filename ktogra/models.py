from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    time = models.DateTimeField()
    home = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='home')
    away = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='away')
    kolejka = models.IntegerField()
    gameweek = models.IntegerField()
    league = models.IntegerField()
    description = models.CharField(max_length=128,default="match")


    def __str__(self):
        return self.description

    class Meta:
        db_table = "matches"



'''class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text'''
