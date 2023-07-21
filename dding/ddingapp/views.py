from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    gongmos = Gongmo.objects.all()
    context = {"gongmos" : gongmos}
    return render(request, "ddingapp/index.html", context)

def gongmoCreate(request):
    if request.method == "POST":
        gongmoForm = GongmoForm(request.POST)
        if gongmoForm.is_valid():
            gongmoPost = gongmoForm.save(commit = False)
            gongmoPost.save()
            return redirect("index")
        else:
            messages.error(request, "폼이 유효하지 않습니다")
    else:
        gongmoForm = GongmoForm()
    context = {"gongmoForm" : gongmoForm}
    return render(request, "ddingapp/gongmoCreate.html", context)

@login_required
def teamCreate(request, gongmoPk):
    gongmo = get_object_or_404(Gongmo, pk=gongmoPk)
    if request.method == "POST":
        teamForm = TeamForm(request.POST)
        if teamForm.is_valid():
            teamPost = teamForm.save(commit=False)
            teamPost.gongmo = gongmo
            teamPost.created_by = request.user
            teamPost.save()
            return redirect("gongmoDetail", gongmoPk=gongmo.pk)
        else:
            messages.error(request, "폼이 유효하지 않습니다")
    else:
        teamForm = TeamForm()
    context = {"teamForm" : teamForm}
    return render(request, "ddingapp/teamCreate.html", context)

def gongmoDetail(request, gongmoPk):
    gongmo = get_object_or_404(Gongmo, pk=gongmoPk)
    teams = Team.objects.filter(gongmo=gongmo)
    context = {"gongmo": gongmo, "teams":teams}
    return render(request, "ddingapp/gongmoDetail.html", context)

@login_required
def teamDetail(request, gongmoPk, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    jickgoons = team.jickgoons.all()
    
    member = team.member_set.filter(user=request.user).first()
    if member:
        member_jickgoon = member.jickgoon.name
    else:
        member_jickgoon = None

    context = {
        'team': team,
        'jickgoons': jickgoons,
        'member_jickgoon': member_jickgoon,
    }
    return render(request, 'ddingapp/teamDetail.html', context)


def gongmoDelete(request, gongmoPk):
    gongmoPost = get_object_or_404(Gongmo, pk=gongmoPk)
    gongmoPost.delete()
    return redirect("index")

def teamDelete(request, gongmoPk, teamPk):
    teamPost = get_object_or_404(Team, pk=teamPk)
    teamPost.delete()
    return redirect("gongmoDetail", gongmoPk=gongmoPk)

@login_required
def teamJoin(request, gongmoPk, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    jickgoons = Jickgoon.objects.filter(name__in=['기획', '개발', '디자인'])
    
    if request.method == 'POST':
        selected_jickgoons_ids = request.POST.getlist('jickgoons')
        selected_jickgoons = Jickgoon.objects.filter(id__in=selected_jickgoons_ids)
        for jickgoon in selected_jickgoons:
            Member.objects.create(user=request.user, team=team, jickgoon=jickgoon)
        return redirect('teamDetail', gongmoPk=gongmoPk, teamPk=teamPk)
    
    context = {
        'team': team,
        'jickgoons': jickgoons,
    }
    return render(request, 'ddingapp/teamJoin.html', context)

@login_required
def mypage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    bookmarks = Bookmark.objects.filter(user=user)
    context = {'user': user, 'bookmarks': bookmarks}
    return render(request, 'ddingapp/mypage.html', context)

@login_required
def bookmark(request, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    user = request.user
    bookmark, created = Bookmark.objects.get_or_create(user=user, team=team)

    if not created:
        bookmark.delete()

    return redirect('teamDetail', gongmoPk=team.gongmo.pk, teamPk=teamPk)