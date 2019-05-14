from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from github import Github
from github.GithubException import UnknownObjectException
from .forms import InfosForm
from gitInsights.models import Repository
from django.contrib.auth.decorators import login_required
import operator
from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# b96a6ca65f3d7a4215efc16c3ed49f5d7ba2763f

#@login_required
def index(request):

    form = InfosForm(request.POST or None)

    if form.is_valid():

        g = Github("b96a6ca65f3d7a4215efc16c3ed49f5d7ba2763f")

        try:

            orga_name = form.cleaned_data['orga_name']
            org = g.get_organization(orga_name)
            repos = org.get_repos()
            reposList = []
            totalCommits = []
            #Transformation de la PaginatedList en liste classique pour manipuler facilement les repos
            for repo in repos:
                commitsList = repo.get_stats_participation().all
                repository = Repository(titre=repo.name, starsgazers=repo.stargazers_count)
                if len(commitsList) >= 2:
                    repository.commits_this_week = commits_this_week=commitsList[-1]
                    repository.commits_last_week = commits_last_week=commitsList[len(commitsList)-2]
                reposList.append(repository)
            reposList.sort(key=lambda x: x.starsgazers, reverse=True)
            reposList = reposList[:10]
            #django jchart
            envoi = True

        except UnknownObjectException :
            erreur = True

    return render(request,'gitInsights/index.html', locals())

def get_total_commits_last_week(reposList):

    totalCommits = []
    for repo in reposList:
        totalCommitsAllWeeks = repo.get_stats_participation().all
        totalCommits.append(totalCommitsAllWeeks[-1])

    return totalCommits

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})
