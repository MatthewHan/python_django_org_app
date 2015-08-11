__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.groups.views import GroupsView, GroupView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', login_required(GroupsView.as_view(), login_url='/users/login/')),
    url(r'^(?P<group_id>\d+)/', login_required(GroupView.as_view(),login_url='/users/login/')),
]