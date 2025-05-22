from django.urls import path
from .views import BlogListView, BlogDetailView, contact_view, create_post_view

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", 
        BlogDetailView.as_view(), name="post_detail"),
    path("contact/", 
        contact_view, name="post_detail"),
    path("post/new/", 
        create_post_view, name="post_detail"),
]