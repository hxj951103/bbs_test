from django.db import models


class User(models.Model):
    SEX = (
        ('M','男'),
        ('F','女'),
        ('U','保密')
    )
    nickname = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    icon = models.ImageField()
    sex = models.CharField(choices=SEX,max_length=8)
    age = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)


