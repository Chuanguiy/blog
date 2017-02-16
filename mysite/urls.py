"""mysite URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import article.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # background administration
    url(r'^$', article.views.home),  # default index
    url(r'^(?P<id_blog>\d+)/$', article.views.detail, name='detail'),  # specify blog which is distinguished by id
    url(r'^Axis/$', article.views.time_axis, name='time_axis'),  # list articles which were sorted by date of publication
    url(r'^tag/(?P<tag>.*?)/$', article.views.classify, name='classify'),  # list articles in same tag
    url(r'^aboutme/$', article.views.my_info, name='aboutme'),  # about me
    url(r'search/$', article.views.search, name="search"),  # search article by title
]

urlpatterns += staticfiles_urlpatterns()
