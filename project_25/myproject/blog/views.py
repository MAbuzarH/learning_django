from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
  query = request.GET.get('q')
  category = request.GET.get('category')
  post = Post.objects.all()
  
  #search using Q objects
  if query:
    post = post.filter(
      Q(title__icontains=query)|
      Q(content__icontains=query)
    )
  
  #filter by category
  if category:
    post = post.filter(category__iexact=category)
    
  return render(request,'blog/post_list.html',{'posts':post,'query':query,'category':category})
