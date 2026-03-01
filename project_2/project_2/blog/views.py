from django.shortcuts import render
from django.http import HttpResponse

def show_blog():
    return '''
    <h1><center>Welcome to the Blog Home Page!</center></h1>
    <p>This is where you can find all the latest posts and updates from our blog.</p>
    <p>Feel free to explore and read our articles on various topics.</p>'''

# Create your views here.
def home(request):
    return HttpResponse(show_blog())

def about(request):
   
    return HttpResponse("<h1><center>About Us</center></h1><p>This is the about page of our blog. We are passionate about sharing knowledge and insights on various topics. Our team of writers is dedicated to providing high-quality content to our readers.</p>") #we can write html here but this is not good practice
