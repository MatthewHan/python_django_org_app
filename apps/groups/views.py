from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Organization
from .forms import OrgForm
class GroupsView(View):
    #New Method and Index Method due to wireframe organization
    def get(self,request):
        print 'in GroupsView get(Index)'
        groups = Organization.objects.annotate(membercount = Count('members'))
        context = {
            'groups': groups,
            'form':OrgForm(),
        }
        return render(request, 'groups/index.html', context)
    #Create Method
    def post(self, request):
        print 'in GroupsView post(Create)'
        form = OrgForm(request.POST)
        if form.is_valid():
            print 'valid form process and create'
            name = request.POST.get('name')
            description = request.POST.get('description')
            creator = User.objects.get(id=request.user.id)
            group = Organization.objects.create(name = name, description = description, creator = creator)
            group.members.add(creator)
            return redirect('/groups')
        else:
            print 'invalid form, send back to display errors'
            groups = Organization.objects.annotate(membercount = Count('members'))
            context = {
                'groups': groups,
                'form':form,
            }
            return render(request, 'groups/index.html', context)
class GroupView(View):
    #Show Method
    def get(self,request, group_id):
        print 'in GroupView get(Show One)'
        group = Organization.objects.get(id=group_id)
        context = {
            'group': group,
        }
        return render(request, 'groups/show.html', context)
    #Update and Destroy Methods due to limitations of Django urls in Restful Routing
    def post(self,request, group_id):
        print 'in GroupView post(Delete)'
        group = Organization.objects.get(id=group_id)
        print request.POST
        if request.POST.get('_method') == 'delete':
            Organization.objects.filter(id=group_id).delete()
        if request.POST.get('_method') == 'patch':
            if request.POST.get('_action') == 'join':
                group.members.add(request.user)
            if request.POST.get('_action') == 'leave':
                group.members.remove(request.user)
        return redirect('/groups')

    #User.interests.add(interest1)
    #userInstance = User.objects.get(id=request.user.id)
    #Organization.members.add(userInstance)