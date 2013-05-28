from django.conf.urls import patterns,url
from pools import views

urlpatterns = patterns('',
        url(r'^/pools$',views.index,name='index')
        url(r'^/two.html$',views.two,name='two'),
                       
                       )
