from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Author, Blog
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    #blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    num_blogs = Blog.objects.count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_blogs": num_blogs,
        "num_authors": num_authors,
        "num_visits" : num_visits,
    }
    return render(request, 'blog/home.html', context = context)

#class MyView(LoginRequiredMixin, view):
#    login_url = '/login/'
#    redirect_field_name = 'redirect_to'

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 2

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context["blog_list"] = Blog.objects.get(self.id)
        #return context