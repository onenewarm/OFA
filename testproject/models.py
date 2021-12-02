from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.dateformat import DateFormat


class User(AbstractUser):
    age = models.IntegerField(default=0)
    mbti = models.CharField(max_length=10)
    job = models.CharField(max_length=30)
    token = models.TextField()
    refresh_token = models.TextField(default="")
    user_seq_no = models.TextField(default="")
    gender = models.CharField(max_length=10)


class Account(models.Model):
    username = models.ForeignKey(
        "testproject.User", on_delete=models.CASCADE)
    account_num = models.TextField()
    account_money = models.TextField()
    bank = models.CharField(max_length=100)


class Subscription(models.Model):
    user_account = models.ForeignKey(
        "testproject.Account", on_delete=models.CASCADE)
    name = models.TextField()
    payment = models.TextField()
    date = models.DateField(default=DateFormat(datetime.now()).format('md'))
    paylink = models.TextField()
    cancellink = models.TextField()


class RecommendSub(models.Model):
    username = models.ForeignKey(
        "testproject.User", on_delete=models.CASCADE)
    name = models.TextField()
    payment = models.TextField()
    paylink = models.TextField()