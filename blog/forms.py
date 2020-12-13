from django.forms import ModelForm

from blog.models import BlogPost

class CreateBlogPostForm(ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']