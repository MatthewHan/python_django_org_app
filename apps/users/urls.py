__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.users.views import UsersView, Login, Register, DisplayUser, DeleteUser, UpdateUser
urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login', name = 'login', kwargs={'template_name': 'users/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout', kwargs={'next_page':'/'}),
    url(r'^register', Register.as_view()),
    # url(r'^(?P<user_id>\d+)/', DisplayUser.as_view()),
    # url(r'^(?P<user_id>\d+)/delete', DeleteUser.as_view()),
    # url(r'^(?P<user_id>\d+)/edit', UpdateUser.as_view()),
]