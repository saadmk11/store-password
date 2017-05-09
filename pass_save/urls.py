from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.details, name='details'),
    url(r'^create/', views.create, name='add_new'),
    url(r'^(?P<id>\d+)/update/', views.update, name='update'),
    url(r'^(?P<id>\d+)/delete/', views.delete, name='delete'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]