from django.shortcuts import render


def home(request):
  return render(request,'base.html')

def about(request):
  student_list = [
    {"name":"Ali","class":"10th"},
    {"name":"abuzar","class":"12th"},
    {"name":"Asif","class":"10th"},
  ]
  return render(request,'blog.html',{'students':student_list})
