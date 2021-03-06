"""ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.static import serve
from ai.settings import STATIC_ROOT,MEDIA_ROOT
from sight.views import UploadView,IndexView,WeixinView,UploadImgView
from sight import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^test/', UploadView.as_view(),name='upload'),
    url(r'^upload', UploadImgView.as_view(),name='upload_local'),
    url(r'^show', views.showImg),
    url(r'^weixin',WeixinView.as_view(),name='weixin_token')

]

