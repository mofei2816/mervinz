# -*- coding:utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2016 Mervin <mofei2816@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from django.conf.urls import url

from blog import views as blog_view
from mervinz import settings

urlpatterns = [
    url(r'^$', blog_view.home),
    url(r'^post/$', blog_view.post),
    url(r'^post/(\d+)/$', blog_view.post_detail),
    url(r'^about/$', blog_view.about),
    url(r'^search/$', blog_view.search),
    url(r'^robots\.txt$', blog_view.robots_txt)
]

if settings.DEBUG:
    urlpatterns.append(url(r'^404/$', blog_view.handler404))
    urlpatterns.append(url(r'^500/$', blog_view.handler500))
