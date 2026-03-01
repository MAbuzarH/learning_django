from django.shortcuts import render
from datetime import datetime


def blog_details(request):
  blogs = [
   {"title":"Django basic","is_featured":False,"author":"zain"} ,
   {"title":"Django basic","is_featured":True,"author":""} ,
   {"title":"Django basic","is_featured":False,"author":"Ali"} 
  ]
  context={
    "blogs":blogs,
    "today":datetime.now(),
    "html_code":"<h1>wellcome to my blog</h1>"
  }
  return render(request,'blog/blog_details.html',context)

