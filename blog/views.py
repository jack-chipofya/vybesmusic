from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post,New,Video

def index(request):
    posts=Post.objects.filter(status=1)
    news=New.objects.all()
    videos=Video.objects.all()
    return render(request,"index.html",{"posts":posts,"news":news,"videos":videos})
def video(request,slug):
    vid=get_object_or_404(Video,slug=slug)
    return render(request,"video.html",{"video":vid})

def news(request,slug):
    news=get_object_or_404(New,slug=slug)
    return render(request,"news.html",{"news":news})
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'details.html'