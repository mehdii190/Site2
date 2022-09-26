from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from .models import Post, comment


def index(request):
    return HttpResponse("salam")

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'posts/post_list.html',context=context)

class PostLits(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound('post is not exist')
    comments = comment.objects.filter(post=post)
    context = {'post':post,'comments':comments}
    return render(request,'posts/post_detail.html',context=context)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    #context_object_name = 'posts'
    #def get_queryset(self):
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        #print(kwargs)
        context['comments']=comment.objects.filter(post=kwargs['object'].pk)
        return context




def post_create(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
    return render(request,'posts/post_create.html',{'form':form})