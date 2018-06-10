"""bbs_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from post import views as post_view
from user import views as user_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', post_view.post_list, name='post_list'),
    url(r'^post/list/', post_view.post_list, name='post_list'),
    url(r'^post/create/', post_view.create, name='post_create'),
    url(r'^post/read/', post_view.read, name='post_read'),
    url(r'^post/edit/', post_view.edit, name='post_edit'),
    url(r'^post/search/', post_view.search, name='post_search'),


    url(r'^user/register/', user_view.register, name='user_register'),
    url(r'^user/login/', user_view.login, name='user_login'),
    url(r'^user/info/', user_view.info, name='user_info'),
    url(r'^user/logout/', user_view.logout, name='user_logout')
]
