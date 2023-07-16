from django.shortcuts import render, redirect, get_object_or_404
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

    try:
        member = team.member_set.get(user=request.user)
        member_jickgoon = member.jickgoon.name
    except Member.DoesNotExist:
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
        form = MemberForm(request.POST)
        if form.is_valid():
            jickgoon_id = request.POST.get('jickgoon')
            jickgoon = get_object_or_404(Jickgoon, id=jickgoon_id)
            member = form.save(commit=False)
            member.team = team
            member.user = request.user
            member.jickgoon = jickgoon
            member.save()
            return redirect('teamDetail', gongmoPk=gongmoPk, teamPk=teamPk)
    else:
        form = MemberForm()
    context = {
        'form' : form,
        'team' : team,
        'jickgoons': jickgoons,
    }
    return render(request, 'ddingapp/teamJoin.html', context)
