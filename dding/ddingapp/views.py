from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.views.decorators.http import require_POST


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

def gongmoDetail(request, pk):
    gongmo = get_object_or_404(Gongmo, pk=pk)
    teams = Team.objects.filter(gongmo=gongmo)
    context = {"gongmo": gongmo, "teams":teams}
    return render(request, "ddingapp/gongmoDetail.html", context)


@require_POST
def teamCreate(request, pk):
    if request.user.is_authenticated:
        gongmo = get_object_or_404(Gongmo, pk=pk)
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.user = request.user
            team.gongmo = gongmo
            team.save()
        return redirect("gongmoDetail", team.pk)
    else:
        messages.warning(request, "팀 생성을 위해서는 로그인이 필요합니다.")
        return redirect("accounts:login")