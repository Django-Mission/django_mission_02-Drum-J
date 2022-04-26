from csv import writer
from re import template
from sys import orig_argv
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request) :
    return render(request, 'index.html')
    
def post_list_view(request) :
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id) :
    return render(request, 'posts/post_detail.html')

@login_required
def post_create_view(request) :
    if request.method == "GET" :
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            iamge=image,
            content=content,
            writer=request.user,
        )
        return redirect('index')   

def post_update_view(request, id) :
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id) :
    return render(request, 'posts/post_confirm_delete.html')   

def url_view(request) :
    print('url_view()')
    data = {'code':'001', 'msg':'ok'}
    return HttpResponse('<h1>안녕</h1>')
    # return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request) :
    print(f'request.method: {request.method}')

    if request.method =='GET' :
        print(f'request.GET: {request.GET}')
    elif request.method =='POST' :
        print(f'request.POST: {request.POST}')
    # print(f'request.GET: {request.GET}')  #GET = 데이터를 받을 때 사용
    # print(f'request.POST: {request.POST}') #POST = 데이터를 추가,수정,삭제 할 때 사용
    return render(request, 'view.html')

    # 이 위까지는 FBV 함수 기반 뷰
    # 밑에서부터는 CBV 클래스 기반 뷰

class class_view(ListView) :
    model = Post
    template_name = 'cbv_view.html'