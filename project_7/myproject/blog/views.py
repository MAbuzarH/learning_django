from django.shortcuts import render
from datetime import datetime

class User:
  def __init__(self,username,user_age):
    self.username = username
    self.user_age = user_age

def home(request):
  context={
    "name": "Abuzar  shah",
    "age":25,
    "skills":["python","java","java script"],
    "user":User("Shah",33),
    "blog":{
      "title":"Python Templates Intro",
      "author":{
        "name":"ali"
      },
      "content":"<b>this is content </b>",
      "created_at":datetime(2025,8,18,10,20)
    },
    "empty_val":None
  }

  return render(request,'blog/home.html',context)

