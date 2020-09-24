from django.shortcuts import render
from .models import Article
from blog_app.form import ArticleForm

x = 0
z =5
# Create your views here.

def blogview(request):
    global x,y,z
    x = 0
    y,z = 5,5
    all_entries = Article.objects.all()[x:y]
    my_dict ={'insert_me': all_entries}
    # print('my_dict::::', my_dict)
    return render(request,'blog_app/base.html',context=my_dict)
def nextview(request):
    global x,y,z
    y = z +5
    # print(f'x::{x},y::{y}')
    all_entries = Article.objects.all()[z:y]
    my_dict ={'insert_me': all_entries}
    z = z + 5
    # print('my_dict::::', my_dict)
    return render(request,'blog_app/base.html',context=my_dict)



def detailview(request,pk):
    # print('pk....:',pk)
    entry = Article.objects.get(pk=pk)
    return render(request,'blog_app/detail.html',{'Entry':entry})

def deleteview(request,pk):
    entry = Article.objects.get(pk=pk)
    entry.delete()
    return blogview(request)


def editview(request,pk):

    count = Article.objects.get(pk=pk)
    form = ArticleForm(instance=count)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=count)
        # print('Request::::::',request.POST)
        if form.is_valid():
            form.save(commit=True)
            return blogview(request)
        else:
            return render(request,'blog_app/create.html',{'form': form})
    else:
        return render(request,'blog_app/create.html',{'form': form})


def createview(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        print('Request::::::',request.POST)
        if form.is_valid():
            form.save(commit=True)
            return blogview(request)
        else:
            # Print('Error in the blog..Please try again!!')
            return render(request,'blog_app/create.html',{'form': form})
    else:
        return render(request,'blog_app/create.html',{'form': form})
