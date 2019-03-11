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
        reposStars = get_repos_stars(repos)
        envoi = True

    return render(request,'gitInsights/index.html', locals())

def informations(request):

    return render(request,'gitInsights/informations.html')

def get_repos_stars(repos):

    reposStars = {}
    for repo in repos:
        reposStars[repo.name] = repo.stargazers_count

    reposStars = {k: v for k, v in sorted(reposStars.items(), key=lambda x: x[1], reverse=True)}
    return reposStars
