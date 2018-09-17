from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # ?P는 패턴 / <pk>는 pk라는 인자로 넘김 / \d 숫자 / +는 계속 확장
    # pk 인자값을 설정한 경우 def post_detail(request, pk)로 view정의
    #/은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
    #$는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]