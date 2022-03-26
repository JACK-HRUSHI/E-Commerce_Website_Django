from django.shortcuts import render
from .models import Blogpost, Suggest

def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post': post})


def suggest(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        suggest = Suggest(name=name, email=email, phone=phone, desc=desc) # Contact() is a constructor of Contact Class
        suggest.save()
        thank = True

        return render(request, 'blog/suggest.html', {'thank': thank})

    return render(request, 'blog/suggest.html')