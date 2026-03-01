from django.shortcuts import render
from datetime import datetime

class User:
  def __init__(self,username,user_age):
    self.username = username
    self.user_age = user_age

def blog_details(request):
  post ={
    "title":"my First blog post",
    "content":"This is content of my first blog post ",
    "author":"Abuzar",
    "created_At":datetime(2025,8,13,10,20),
    "comment_count":5,
    "tags":["Django","Python","Web development"],
    "price":100,
    "number":7
  }
  return render(request,'blog/blog_details.html',{"post":post})

