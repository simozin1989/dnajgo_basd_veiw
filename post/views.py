from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from .models import Post 




# Create your views here.
class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    
    
class PostDetail(DetailView):
    model = Post
  
    
class PostCreat(CreateView):
    model = Post    
    
class PostUpdate(UpdateView):
    model = Post      
    
    
    
    
    
class PostDetete(UpdateView):
    model = Post        
      