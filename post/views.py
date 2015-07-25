from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from post.models import Post
from django.shortcuts import render_to_response

# Create your views here.


def home(request):
	posts = Post.objects.all()
	return render_to_response('index.html', {"posts": posts})

def post_view(request, post_id):
    post = Post.objects.get(pk = post_id)
    return render_to_response('post.html', {"post": post})


class PostsList(ListView):
	model = Post
	template_name = "index.html"

    # def head(self, *args, **kwargs):
    #     posts = self.objects.all()
    #     response = HttpResponse('')
    #     # RFC 1123 date format
    #     response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    #     return response

