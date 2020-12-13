from django.shortcuts import render, redirect

from blog.models import BlogPost
from account.models import Account
from blog.forms import CreateBlogPostForm

def create_blog_view(request):
	
	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_autenticate')
	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		obj = form.save(commit = False)
		author = Account.objects.filter(email= user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
	
	context['form']	= form
	return render(request,'blog/create_blog.html', {})

