from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Post

from .blogform import BlogPostForm

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .signup_form import  SignUpForm


def home(request):
    blogs = Post.objects.only('title','body','image','created_at','description')
    return render(request,'index.html',{"blogs":blogs})


@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Uploaded your Post")
            return redirect('home')  
    else:
        form = BlogPostForm()
    
    return render(request, 'create_post.html', {'form': form})

def post(request,id):
    blog = get_object_or_404(Post, id=id)

    return render(request,"blog.html",{"blog":blog})


def login_view(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')  # Redirect to a specific page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
     else:

        form = AuthenticationForm()
    
     return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registeration Succesful")
            return redirect('home')
        else:
            messages.error("Error in registration")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

    
