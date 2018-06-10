from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from user.forms import RegisterForms
from user.models import User
from user.helper import login_require

def register(request):
    if request.method == 'POST':
        register_form = RegisterForms(request.POST, request.FILES)
        if register_form.is_valid():
            # 保存数据
            user = register_form.save(commit=True)
            # 将密码加密
            user.password = make_password(user.password)
            user.save()
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            return redirect('/user/info/')
        else:
            return render(request, 'register.html', {'error': register_form.errors})
    return render(request, 'register.html', {})

def login(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        passowrd = request.POST.get('password')
        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': '用户名错误'})
        if check_password(passowrd, user.password):
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            return redirect('/user/info/')
        else:
            return render(request, 'login.html', {'error': '密码错误'})
    return render(request, 'login.html', {})


@login_require
def info(request):
    uid = request.session['uid']
    user = User.objects.get(id=uid)
    return render(request, 'user_info.html', {'user':user})

@login_require
def logout(request):
    # 删除session
    request.session.flush()
    return redirect('/user/login/')
