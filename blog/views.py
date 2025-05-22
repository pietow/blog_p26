from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html" 
 
class BlogDetailView(DetailView):
    model= Post
    template_name = "post_detail.html"

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Normally you might send an email or save the message
            return render(request, 'thanks.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import PostForm

def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            form.save()
            return render(request, 'thanks.html', {'name': author})
    else:
        form = PostForm()
    return render(request, 'contact.html', {'form': form})
