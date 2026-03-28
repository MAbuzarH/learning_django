from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def show_msg(request):
  messages.debug(request,'this is  debug message')
  messages.info(request,'this is  info message')
  messages.success(request,'this is  success message')
  messages.warning(request,'this is  warning message')
  messages.error(request,'this is  error message')
  return render(request,'message.html')

  
