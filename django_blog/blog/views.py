from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.urls import reverse_lazy


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {'form': form})


def login(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')


def logout(request):
    return auth_views.LogoutView.as_view(template_name='registration/logout.html')



## CRUD operations for Blog posts

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    success_url = 'post_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("You are not allowed to delete this post")
        return obj



## CRUD operations for Comments

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    success_url = 'comment_list'
    
class CommentCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('comment_list')
    
class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('comment_list')
    
class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('comment_list')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("You are not allowed to delete this comment")
        return obj


## Search posts

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)).distinct()
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})


## Post by Tags

class PostByTagView(ListView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = 'post_list'
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        return Post.objects.filter(tags__name__in=[self.tag.name])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context