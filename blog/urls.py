from django.conf.urls import url
from . import views

urlpatterns = [
    ##url(r'^$', views.post_list, name='post_list'),
    url(r'^courses/', views.course_list, name='course_list'),
    url(r'^$', views.home, name='home')
]
