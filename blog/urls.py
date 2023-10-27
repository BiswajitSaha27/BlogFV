from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blogs/', views.BlogListView.as_view(), name="all_blogs"),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
    path('authors/', views.AuthorListView.as_view(), name="all_authors"),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name="author_detail"),
]