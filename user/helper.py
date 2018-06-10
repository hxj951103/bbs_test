from django.shortcuts import render
from django.shortcuts import redirect


# 自定义装饰器,验证用户是否登录
def login_require(view_func):
    def warp(request):
        if request.session.get('uid'):
            return view_func(request)
        else:
            return redirect('/user/login')
    return warp


