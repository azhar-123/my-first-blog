
"""
A view is a place where we put the "logic" of our application. 
It will request information from the model you created before and pass it to a template

"""

from django.shortcuts import render
from .models import Post                                    # Now is the moment when we have to include the model we have written in models.py             

from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # newly added and 
	return render(request,'blog/post_list.html',{'posts':posts})                           # newly added before --> {}



def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)

	return render(request,'blog/post_detail.html',{'post':post})
	


