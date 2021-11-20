from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from .models import Post 




# Create your views here.
class PostList(ListView):
    model = Post
    #context_object_name = 'posts'  ## in template [ object_list , post_list ]
    ordering = ['craet_at']
    # queryset = Post.objects.filter(active=True)
    # template_name = 'post/test.html'
    
    def get_queryset(self):
       return Post.objects.filter(active=True)
   
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       #you can call anther model her and geve it to context
       context['my_name'] = 'Alilou mohamed'
       return context
   
   
    
class PostDetail(DetailView):
    model = Post
  
    
class PostCreat(CreateView):
    model = Post    
    
class PostUpdate(UpdateView):
    model = Post      
    
    
    
    
    
class PostDetete(UpdateView):
    model = Post        
      