from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Author
 
def home(request):
    return render(request,'home.html')

def get_blog(request):
    blogs=Blog.objects.all()
    return render(request,"index.html",{"blogs":blogs})
 
def get_first(request):
    blog_first=Blog.objects.first()
    return render(request,"first.html",{"blogs":blog_first})
    
def get_author(request): 
    authors=Author.objects.all()
    # print(authors.first().author_blogs.all() )
    return render(request,"front.html",{"authors":authors})
 
def filter_with_s(request):
    start_s=Blog.objects.filter(title__startswith='S')
    print(start_s)
    return render(request,"first.html",{"st":start_s})



