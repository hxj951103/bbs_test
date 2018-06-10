from django.shortcuts import render, redirect
from math import ceil

from post.models import Post
from post.helper import page_cache
from user.helper import login_require


@login_require
def create(request):
	'''create model'''
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		post = Post.objects.create(title=title, content=content)
		return redirect('/post/read/?post_id=%d' % post.id)
	return render(request, 'create.html')


def read(request):
	post_id = int(request.GET.get('post_id'))
	try:
		post = Post.objects.get(id=post_id)
		return render(request, 'read.html', {'post': post})
	except Post.DoesNotExist:
		return redirect('/')

@page_cache(10)
def post_list(request):
	'''
	首页显示数据
	'''
	page = int(request.GET.get('page', 1))
	# 页面显示条数
	per_page = 3
	total = Post.objects.count()
	pages = ceil(total/per_page)

	start_post = (page-1) * per_page
	end_post = page * per_page
	posts = Post.objects.all().order_by('-created')[start_post:end_post]
	return render(request, 'post_list.html', {'posts': posts, 'pages':range(pages)})


@login_require
def edit(request):
	if request.method == 'POST':
		post_id = int(request.POST.get('post_id'))
		title = request.POST.get('title')
		content = request.POST.get('content')

		post = Post.objects.get(id=post_id)
		post.title = title
		post.content = content
		post.save()
		return redirect('/post/read/?post_id=%d' %post_id)
	else:
		post_id = int(request.GET.get('post_id'))
		post = Post.objects.get(id=post_id)
		return render(request, 'edit.html', {'post': post})


def search(request):
	keyword = request.POST.get('keyword')
	posts = Post.objects.filter(content__contains=keyword)
	return render(request, 'search.html', {'posts':posts})