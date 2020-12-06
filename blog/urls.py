from django.urls import path
from blog.views import (
	create_blog_view,
	)

app_name = 'blog' # Если мы создаём urls.py в приложении, а не в mysite,
#					мы должны reference на приложение в котором создали urls

urlpatterns = [
	path('create',create_blog_view, name = 'create'),
	
]
