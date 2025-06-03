from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import ContactForm, PostForm
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy

def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = PostForm()
        return render(request, 'contact.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(form.cleaned_data)
            return render(request, 'thanks.html', form.cleaned_data)
            # return render(request, 'thanks.html', {'name': name})
        else:
            return HttpResponseForbidden('Failed') 
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

class BlogListView(ListView):
    model = Post
    template_name = "home.html" 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['post_list'] = context['post_list'].filter(body="hello world")
        return context
 
class BlogDetailView(DetailView):
    model= Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model= Post
    template_name = "post_new.html"
    fields = ['title', 'author', 'body']
    # fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')