from .forms import ChoiceForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages

from .models import Choice, Question
# Create your views here.
def savollar(request):
    # bu yirda question modelidan barcha objektlar olinadi
    savollar = Question.objects.all()
    return render(
        request, 'questions/savollar.html', {'savollar': savollar})


def savol_detail(request, id):
    # bu yirda Question modelidan id is parametirda kelayotgan 
    # id ga teng teng bo'lgan objekt olinadi 
    savol = get_object_or_404(Question, id=id)
    return render(request, 'questions/savol.html',{"savol":savol})

def check_answer(request, variant_id):
    # bu yirda Choice modiling id si teng bolgan objekt olinadi
    # nariant_id ga teng bo'lgan objekt olinadi
    javob = get_object_or_404(Choice, id=variant_id)
    correct = javob.is_correct
    return render(request, 'questions/checked.html', {'correct': correct})

def creat_question(request):
    if request.method == "POST":
       question = request.POST.get('question') 
       Question.objects.create(question=question)
       return redirect("poll:savollar")
    return render(request, 'questions/creat_question.html')

def create_group(request):
    if request.method == "POST":
       group = request.POST.get('group') 
       Group.objects.create(name=group)
       return redirect("poll:groups")
    return render(request, 'accounts/create_group.html')

def group(request):
    groups = Group.objects.all()
    return render(request, 'accounts/groups.html', {'groups': groups})

def remove_group(request, id):
    group = get_object_or_404(Group, id=id)
    name = group.name()
    group.delete()
    messages.add_message(request, level=messages.WARNING, message=f"Group [ {name} ] muvoffaqiyatli o'chirildi!")
    return redirect("poll:groups")


def edit_group(request, id):
    group = get_object_or_404(Group, id=remore_group)
    if request.method == "POST":
        name = request.POST.get('name')
        group.name = name
        group.save()
        messages.add_message(request, level=messages.SUCCESS, message=f"Group[ {name} ] muvoffaqiyatli o'zgartirildi!")
        return redirect("poll:groups")
#=================================================================================
def create_choice(request):
    form = ChoiceForm()
    if request.method =="POST":
        form = ChoiceForm(data=request.POST)
        if form.is_valid():
            choice = form.save()
            return redirect("poll:savollar")
    return render(request, 'questions/create_choice.html',{"form":form})


