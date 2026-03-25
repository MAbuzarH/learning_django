from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact


def contact_form(request):
  return render(request, 'contact_form.html')

def submit_contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    message = request.POST.get('message')
    if name and message:
      Contact.objects.create(name=name, message=message)
      return HttpResponse(f'{name} Contact submitted successfully!')
    else:
      return HttpResponse('Name and message are required.', status=400)
  return redirect('contact_form')
    


