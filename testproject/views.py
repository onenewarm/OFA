from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


from .models import User, Account,RecommendSub
import requests
import json
from . import usedTimeRec
from . import profileRec


API_KEY = "95c66bc3-af0c-45b6-8454-6b26bb60c968"
client_secret = "4108142a-0848-452c-b514-cd492222202a"
URL = "https://testapi.openbanking.or.kr"


def home(request):
    return render(request, 'home.html')


def account(request):
    accounts = Account.objects.filter(username=request.user.id)
    return render(request, 'account.html', {'accounts': accounts})


def sub(request):
    return HttpResponse("this page show subscription")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/testproject')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                first_name=request.POST['first name'],
                last_name=request.POST['last name'],
                age=request.POST['age'],
                job=request.POST['job'],
                mbti=request.POST['mbti']
            )
            return redirect('/testproject')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def detail_sub(request):
    return HttpResponse("this page show detail about one sub")


def recommend_sub(request):
    using_id=request.user.username
    user_using_id=User.objects.get(username=using_id)
    usedTimeRec_result=[]
    profileRec_result=[]
    usedTimeRec_result=usedTimeRec.usedTimeRec(using_id)
    profileRec_result=profileRec.profileRec(using_id)
    for i in range(len(usedTimeRec_result)):
        profileRec_result.append(usedTimeRec_result[i])
    combine_list=profileRec_result
    set(combine_list)
    list(combine_list)
    RecommendSub.objects.update_or_create(username=user_using_id, name=combine_list)
    return render(request, 'recommend_sub.html', {
        'recData':combine_list
    })


def logout(request):
    auth.logout(request)
    return redirect('/testproject')


def userauth(request):
    if request.method == "GET":
        code = request.GET['code']
        header = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        param = {
            "code": code,
            "client_id": API_KEY,
            "client_secret": client_secret,
            "redirect_uri": "http://127.0.0.1:8000/testproject/user/auth",
            "grant_type": "authorization_code"
        }
        res = requests.post(URL+'/oauth/2.0/token',
                            params=param, headers=header)
        res = res.json()
        User.objects.update_or_create(username=request.user.username,
                                      defaults={'token': res['access_token'],
                                                'refresh_token': res['refresh_token'],
                                                'user_seq_no': res['user_seq_no']})
        return redirect('/testproject')

        # Create your views here.


def register_account(request):
    return redirect("/testproject")


def loadcsv(request):
    import csv
    import pandas as pd

    with open('C:/Users/gao45/Desktop/OFA/one_for_all/testproject/user_data.csv','r') as f:
        dr=csv.DictReader(f)
        s=pd.DataFrame(dr)
    ss=[]
    for i in range(len(s)):
        st=(s['id'][i],s['gender'][i],s['job'][i],s['age'][i],s['MBTI'][i])
        ss.append(st)
    for i in range(len(s)):
        User.objects.create_user(
                    username=ss[i][0],
                    password="123123",
                    age=ss[i][3],
                    job=ss[i][2],
                    mbti=ss[i][4],
                    gender=ss[i][1]
                )