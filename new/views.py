from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404 
from django.http import JsonResponse

from .models import New, Comment, Like, Dislike
from .forms import NewForm, NewFormMine, CommentForm

class News(ListView):
    queryset = New.objects.all().order_by('-created')
    template_name = 'new/news_list.html'

    paginate_by: int = 6

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

news_list = News.as_view()


    # bunyirda new methodidagi barcha objekit, yangi ikki yoki uc kundan ortiq 
    # objekitni odik 
    # bu narsa QUERESET diyiladi
    # quereset ucun model method iwlamaydi
    
    # contex dictionary  bu tempilitga berib yuboriladingn ozgaruvcilar toplami   


def news_detail(request, id):
    new = get_object_or_404(New, id=id)
    form = CommentForm()
    # bitta nevni olyapmiz nev degan modelni barca metodlari icidan 
    # wu narsa object diyiladi
    # model methodlari faqat objekit ucun iwlaydi....

    if request.method == "POST":
        #comment formaga postda kelayorgan malumotlarni
        # berib validatsiyadan otqazamkiz
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = new
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save() 
            return redirect("new:detail", id=id)
    return render(request, 'new/news_detail.html', {'new': new, "form": form})

def create(request):
    form = NewForm
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect("new:list")
    return render(request, 'new/create.html', {"form": form})

def remove(request, id):
    new = get_object_or_404(New, id=id)
    new.delete()
    return redirect("new:list")

def my_news(request):
    news = New.objects.filter(author=request.user).order_by('-created')
    return render(request, 'new/my_news.html', {'news': news})


def my_create(request):
    form = NewFormMine()
    if request.method == 'POST':
        form = NewFormMine(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect("new:my_news")
    return render(request, 'new/create.html', {"form": form})


def my_update(request, id):
    new = get_object_or_404(New, id=id)
    form = NewFormMine(instance=new)
    if request.method == 'POST':
        form =NewFormMine(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            return redirect("new:my_news")
    return render(request, 'new/create.html', {'form': form})


def my_detail(request, id):
    new = get_object_or_404(New, id=id)

    return render(request, 'new/my_detail.html', {'new': new})


def like(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.dislikes.filter(user=request.user).exists():
            new.dislikes.get(user=request.user).delete()

        if new.likes.filter(user=request.user).exists():
            new.likes.get(user=request.user).delete()
            return JsonResponse({
                "success": True,
                "message": "siz riyaksangizni qaytarib oldingiz!",
                "likes": new.like_count(),
                "dislikes": new.dislike_count()
                }
            )

        Like.objects.create(user=request.user, post=new)
        return JsonResponse({
            "success": True,
            "message": "sizga yoqgan postlar safiga qo'shildi!",
           "likes": new.like_count(),
           "dislikes": new.dislike_count()
            }
        )

    return JsonResponse({
            "success": False,
            "message": "postga riyaksiya qoldirish uchun iltimos ro'yxatdan o'ting!",
            }
        )



def dislike(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.likes.filter(user=request.user).exists():
            new.likes.get(user=request.user).delete()

        if new.dislikes.filter(user=request.user).exists():
            new.dislikes.get(user=request.user).delete()
            return JsonResponse({
                "success": True,
                "message": "siz riyaksangizni qaytarib oldingiz!",
                "likes": new.like_count(),
                "dislikes": new.dislike_count()
                }
            )

        Dislike.objects.create(user=request.user, post=new)
        return JsonResponse({
            "success": True,
            "message": "sizga yoqmagan postlar safiga qo'shildi!",
            "likes": new.like_count(),
            "dislikes": new.dislike_count()
            }
        )

    return JsonResponse({
            "success": False,
            "message": "postga riyaksiya qoldirish uchun iltimos ro'yxatdan o'ting!",
            }
        )