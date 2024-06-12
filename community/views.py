from django.shortcuts import render, redirect
from community.forms import *

# Create your views here.
def index(request):
    form = Form()
    return render(request, 'community/index.html', {'form':form})

def write(request):   
    form = Form()

    return render(request, 'community/write.html', {'form':form})

def list(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    
    articleList = Article.objects.all()
    return render(request, 'community/list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'community/view.html', {'article':article})

def updateform(request, num):
    #article = Article.objects.get(id=num)
    form = Form()
    
    return render(request, 'community/updateform.html', {'form':form})

def delete(request, num):
    contents = Article.objects.get(id=num)
    contents.delete()