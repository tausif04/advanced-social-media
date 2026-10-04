from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, RegisterForm
from .models import Post


def home(request):
    posts = Post.objects.select_related('author').all()

    search = request.GET.get('search', '').strip()
    media = request.GET.get('media', '')
    user_id = request.GET.get('user', '')
    sort = request.GET.get('sort', 'latest')

    if search:
        posts = posts.filter(content__icontains=search)

    if media == 'image':
        posts = posts.filter(image__isnull=False).exclude(image='')
    elif media == 'text':
        posts = posts.filter(image__isnull=True) | posts.filter(image='')

    if user_id:
        posts = posts.filter(author_id=user_id)

    if sort == 'oldest':
        posts = posts.order_by('created_at')
    else:
        posts = posts.order_by('-created_at')

    context = {
        'posts': posts,
        'users': User.objects.filter(posts__isnull=False).distinct().order_by('username'),
        'search': search,
        'media': media,
        'selected_user': user_id,
        'sort': sort,
    }
    return render(request, 'posts/home.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user).select_related('author')

    search = request.GET.get('search', '').strip()
    media = request.GET.get('media', '')
    sort = request.GET.get('sort', 'latest')

    if search:
        posts = posts.filter(content__icontains=search)
    if media == 'image':
        posts = posts.filter(image__isnull=False).exclude(image='')
    elif media == 'text':
        posts = posts.filter(image__isnull=True) | posts.filter(image='')
    posts = posts.order_by('created_at' if sort == 'oldest' else '-created_at')

    return render(request, 'posts/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'search': search,
        'media': media,
        'sort': sort,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post published.')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'title': 'Create Post'})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'title': 'Edit Post'})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('home')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})
