from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import create_update_post
from .models import blogs

# def blog_view(request):
#     # blog_list = blogs.objects.all()
#     blog_list = blogs.objects.filter(status='POP').order_by('-modified_datetime')
#     return render(request, 'Blog/blog.html', {'blog_lists': blog_list})

class PostListView(generic.ListView):
    model = blogs
    template_name = 'Blog/blog.html'
    context_object_name = 'blog_lists'


# def blog_detail_view(request, pk):
#     # return HttpResponse(f'test: {pk}')
#     # finding pk in the database:
#     # post = blogs.objects.get(pk=pk)
#     # using the below code to show 4o4 when pk does not exist on the url
#     post = get_object_or_404(blogs, pk=pk)
#     return render(request, 'Blog/blog_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = blogs
    template_name = 'Blog/blog_detail.html'
    context_object_name = 'post'

# def create_post_view(request):
#     if request.method == 'POST':
#         new_form = create_post(request.POST)
#         if new_form.is_valid():
#             new_form.save()
#             return redirect('blog')
#
#     else:
#         form = create_post()
#     return render(request, 'Blog/create_post.html', context={'form':form})
#     # if request.method == 'POST':
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #
#     #     user1 = User.objects.all()[0]
#     #     blogs.objects.create(title=post_title, text=post_text, status='POP', author=user1)
#     # return render(request, 'Blog/create_post.html')


class PostCreateView(generic.CreateView):
    form_class = create_update_post
    template_name = 'Blog/create_post.html'

# def update_post(request, pk):
#     update_form = get_object_or_404(blogs, pk=pk)
#     form = create_post(request.POST or None, instance=update_form)
#     if form.is_valid():
#         form.save()
#         return redirect('blog')
#     return render(request, 'Blog/create_post.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    model = blogs
    form_class = create_update_post
    template_name = 'Blog/create_post.html'
    context_object_name = 'form'



# def delete_post(request, pk):
#     post = get_object_or_404(blogs, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog')
#     return render(request, 'Blog/post_delete.html', context={'data': post})


class PostDeleteView(generic.DetailView):
    model = blogs
    template_name = 'Blog/post_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('blog')
