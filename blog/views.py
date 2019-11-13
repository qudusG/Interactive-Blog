from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm

def index(request):
	articles = Post.objects.filter(date__year=2019, status=1)
	context = {'articles': articles}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	article = get_object_or_404(Post, pk = post_id)
	comments = Comment.objects.filter(post=article)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(author=form.cleaned_data["author"],
				reply=form.cleaned_data["reply"], post=article)
			comment.save()
			form = CommentForm()
			return HttpResponseRedirect(reverse('blog:detail', args=(article.id,)))
	
	context = {'article':article,'comments':comments,'form':form}
	return render(request, 'blog/detail.html', context)

def signup(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = password)
			login(request, user)
			return HttpResponseRedirect(reverse('blog:index'))
	else:
		form = RegistrationForm()
	return render(request, 'blog/signup.html',{'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return HttpResponseRedirect(reverse('blog:index'))
			else:
				messages.error(request, "invalid username or password")
		else:
				messages.error(request, "invalid username or password")
	form = AuthenticationForm()
	return render(request, 'blog/login.html',{'form':form})

def logout_view(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect('blog:index')
			
def profile(request):
	return HttpResponse('Profile')
