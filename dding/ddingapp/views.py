from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.html import escape
from django.utils import timezone

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
            teamForm.save_m2m()
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
    bookmarks = team.bookmark_set.all()
    
    member = team.member_set.filter(user=request.user).first()
    if member:
        member_jickgoon = member.jickgoon.name
    else:
        member_jickgoon = None


    context = {
        'team': team,
        'jickgoons': jickgoons,
        'member_jickgoon': member_jickgoon,
        'bookmarks' : bookmarks,
        'dev_capacity': team.get_dev_capacity(),
        'plan_capacity': team.get_plan_capacity(),
        'design_capacity': team.get_design_capacity(),
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
        team.member_set.filter(user=request.user).delete()
        
        dev_capacity = team.dev_capacity
        plan_capacity = team.plan_capacity
        design_capacity = team.design_capacity

        member_counts = {
            '개발': team.member_set.filter(jickgoon__name='개발').count(),
            '기획': team.member_set.filter(jickgoon__name='기획').count(),
            '디자인': team.member_set.filter(jickgoon__name='디자인').count(),
        }       

        for jickgoon_id in selected_jickgoons_ids:
            jickgoon = get_object_or_404(Jickgoon, id=jickgoon_id)

            if (jickgoon.name == '개발' and member_counts['개발'] >= dev_capacity) or \
               (jickgoon.name == '기획' and member_counts['기획'] >= plan_capacity) or \
               (jickgoon.name == '디자인' and member_counts['디자인'] >= design_capacity):
                messages.error(request, f"{jickgoon.name} 직군의 참가 인원 수가 이미 초과되었습니다.")
                return redirect('teamDetail', gongmoPk=gongmoPk, teamPk=teamPk)

            Member.objects.create(user=request.user, team=team, jickgoon=jickgoon)
            member_counts[jickgoon.name] += 1
        
        
        notification_message = f"{escape(request.user.username)} 님이 {escape(team.name)} 팀에 {escape(jickgoon.name)} 직군으로 참여하였습니다. ({timezone.now()})"
        notification = Notification.objects.create(user=request.user, team=team, jickgoon=jickgoon, message=notification_message)

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
    teams = Team.objects.filter(member__user=user)
    teamsteams = Team.objects.filter(created_by=user)
    notifications = Notification.objects.filter(team__created_by=user)
    context = {
        'user': user,
        'bookmarks': bookmarks,
        'teams':teams,
        'teamsteams': teamsteams,
        'notifications': notifications,
        }
    return render(request, 'ddingapp/mypage.html', context)

@login_required
def bookmark(request, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    user = request.user
    bookmark, created = Bookmark.objects.get_or_create(user=user, team=team)

    if not created:
        bookmark.delete()

    return redirect('teamDetail', gongmoPk=team.gongmo.pk, teamPk=teamPk)

@login_required
def leaveTeam(request, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    try:
        member = Member.objects.get(user=request.user, team=team)
        member.delete()
    except Member.DoesNotExist:
        pass 
    return redirect(reverse('mypage', args=[request.user.id]))
