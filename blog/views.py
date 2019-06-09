from django.shortcuts import render
#include code we have written in different files
#the . means current directory or current application
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    #create a query set to take actual blog posts from the post model
    posts = Post.objects.filter(published_date__lte
    =timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',
    {'posts' : posts})
