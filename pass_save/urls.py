from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<id>\d+)/update/', views.update, name='update'),
    url(r'^(?P<id>\d+)/delete/', views.delete, name='delete'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]