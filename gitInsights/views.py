from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from github import Github
from .forms import InfosForm

# b96a6ca65f3d7a4215efc16c3ed49f5d7ba2763f
def index(request):



    form = InfosForm(request.POST or None)

    if form.is_valid():

        g = Github("b96a6ca65f3d7a4215efc16c3ed49f5d7ba2763f")
        orga_name = form.cleaned_data['orga_name']
        org = g.get_organization(orga_name)
        repos = org.get_repos()
        count_repos = repos.totalCount
        envoi = True

    return render(request,'gitInsights/index.html', locals())
