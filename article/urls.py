from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mypoject.views.home', name='home'),
    url(r'^', 'article.views.articles'),
    )