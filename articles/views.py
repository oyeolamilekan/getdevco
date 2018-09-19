import re
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.
def n_index(request):
    return render(request,'frst.html',{})

@login_required(login_url='/accounts/login/')
def article_list(request):
    userr = Article.objects.order_by('-id')
    return render(request,'articles_list.html',{'user':userr})

@login_required(login_url='/accounts/login/')
def articles_detail(request,pk):
    article = get_object_or_404(Article,id=pk)
    return render(request,'article_details.html',{'article':article})

@login_required(login_url='/accounts/login/')
def new_post(request):
    found_name = False
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_posts = form.save(commit=False)
            new_posts.user = request.user
            regex = r'\w+'
            list_of_words = re.findall(regex, new_posts.body)
            for listt in list_of_words:
                if str(listt) == str(request.user):
                    found_name = True
                    break
            if found_name:
                new_posts.save()
                return JsonResponse({'status':'ok','reverse_url':f'http://{request.get_host()}/article_detail/{new_posts.id}/'})
            else:
                return JsonResponse({'status':'ko'})
    return render(request, 'new_article.html',{'form':form})

@login_required(login_url='/accounts/login/')
def edit_post(request,id):
    post = get_object_or_404(Article, id=id)
    if post.user == request.user:
        if request.method != 'POST':
            form = ArticleForm(instance=post)
        else:
            form = ArticleForm(instance=post,data=request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                regex = r'\w+'
                list_of_words = re.findall(regex, new_form.body)
                for listt in list_of_words:
                    if str(listt) == str(request.user):
                        found_name = True
                        break
                if found_name:
                    new_form.save()
                    return JsonResponse({'status':'ok','reverse_url':f'http://{request.get_host()}/article_detail/{new_form.id}/'})
                else:
                    return JsonResponse({'status':'ko'})
    else:
        return HttpResponse('not your article')
    return render(request, 'edit_post.html',{'form':form})

@login_required(login_url='/accounts/login/')
def delete_post(request,id):
    post = get_object_or_404(Article, id=id)
    if post.user == request.user:
        post.delete()
        return redirect('/articles/')
    else:
        return HttpResponse('Not your article')
        

