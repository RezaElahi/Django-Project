from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts_list=[
    {
        'author':'Rezo',
        'title':'blog post 1',
        'content':"First post content",
        'date_posted':'August 27, 2018'
    },
    {
        'author':'Karim',
        'title':'blog post 2',
        'content':"Second post content",
        'date_posted':'September 2, 2018'
    }
]

# Create your views here.
# By default the first argument of render is request.
def home(request):
    context ={"posts":Post.objects.all()}
    # Pass a dictionary to the template
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title':'About'})
    
    