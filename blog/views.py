from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def projects(request):
    return render(request, 'blog/projects.html')

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print("New message:", name, email, message)

        messages.success(request, "Your message has been sent!")
        return redirect('contact') 

    return render(request, 'blog/contact.html')
