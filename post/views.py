from account.forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Tag
# Create your views here.
def index(request):
    form = UserForm()
    return render(request, 'post/index.html', {'form':form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/postlist.html', 
        {
        'posts':posts
        })

def post_create(request):
    if request.method == 'GET':
        return render(request, 'post/new_post.html')
    elif request.method == 'POST' :
        new_post = Post()
        new_post.writer = request.user
        new_post.title = request.POST['title']
        new_post.content = request.POST['content']
        new_post.save()
        #  본문의 내용을 띄어쓰기로 잘라낸다.
        words = new_post.content.split(' ')
        # 만약 단어가 #로 시작하면, #를 뗀 후 tag_list에 모아둔다.
        tag_list = []
        for w in words:
            if w[0] == '#':
                tag_list.append(w[1:])
        # 해시태그가 들어있는 리스트를 하나씩 돌면서
        for t in tag_list:
            # 기존에 존재하는 태그면 get, 없으면 create
            tag, boolean = Tag.objects.get_or_create(name=t)
            # 이후 태그 필드에 추가
            new_post.tags.add(tag.id)
        return redirect('post:detail', new_post.id)
    
        

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        #filter에 post 객체 그대로 넣어주기
        comments = Comment.objects.filter(post=post)
        return render(request, 'post/postdetail.html', {
            'post': post,
            'comments':comments,
        })
    elif request.method == 'POST':
        new_comment = Comment()
        #foreignkey > post 객체 직접 넣어주기
        new_comment.post = post
        #foreignkey > request.user 객체 직접 넣어주기
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.save()
        return redirect('post:detail', post_id)


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        return render(request, 'post/postupdate.html', {
            'post': post,
        })
    elif request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        #foreignkey인 writer field는 직접 객체를 찾아서 넣어준다.
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        #  본문의 내용을 띄어쓰기로 잘라낸다.
        words = post.content.split(' ')
        # 만약 단어가 #로 시작하면, #를 뗀 후 tag_list에 모아둔다.
        tag_list = []
        for w in words:
            if w[0] == '#':
                tag_list.append(w[1:])
        # 해시태그가 들어있는 리스트를 하나씩 돌면서
        for t in tag_list:
            # 기존에 존재하는 태그면 get, 없으면 create
            tag, boolean = Tag.objects.get_or_create(name=t)
            # 이후 태그 필드에 추가
            post.tags.add(tag.id)
        return redirect('post:detail', post.id)
    
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'post/tag_list.html', {
        'tags':tags,
    })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'post/tag_posts.html', {
        'tag':tag,
        'posts':posts
    })