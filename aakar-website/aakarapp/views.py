from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
import pandas as pd
import numpy as np
from ranklist import df

## import data tables from database
from .models import TaskZero

print(f"df from views : {df} ")

# Create your views here.

def home(request):
    return render(request, "home.html")

def dashboard(request):
    user = request.user
    print(f"user.id: {user.id}")
    data = SocialAccount.objects.get(user=user).extra_data
    email = data.get('email')
    name = data.get('name')
    name = name.split(" ")
    picture = data.get('picture')
    current_user_id = 220000 + user.id

    rank_list = np.array(df['CRID']=="AK"+str(current_user_id))

    rank = -1
    print(rank_list)
    for i in range(len(rank_list)):
        if rank_list[i]:
            rank = i+1
            break
    
    objects = TaskZero.objects.all()
    return render(request, "dashboard.html", {'email': email, "name":name[0], "picture": picture, "CRID":"AK"+str(current_user_id), "rank":rank, "objects":objects})

