
"""
A view is a place where we put the "logic" of our application. 
It will request information from the model you created before and pass it to a template

"""

from django.shortcuts import render
# from .models import Post                                    # Now is the moment when we have to include the model we have written in models.py             

from django.utils import timezone

def post_list(request):

	# Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{})