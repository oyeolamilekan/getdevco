from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from articles.models import Article
from .forms import UserRegistrationForm,ProfileRegsitrationForm,LoginForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        next_page = request.POST.get('next')
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = ProfileRegsitrationForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet

            new_user = user_form.save(commit=False)
            new_user_p = profile_form.save(commit=False)

            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user_p.user = new_user
            new_user_p.save()

            authenticated_user = authenticate(username=new_user.username, password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegsitrationForm()
    return render(request, 'register.html', {'form': user_form,'form_2':profile_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.profile:
                    login(request, user)
                    next_page = request.POST.get('next')
                    if next_page:
                        return JsonResponse({'redirect':'http://'+request.get_host()+next_page})
                    else:
                        return JsonResponse({'redirect':'http://'+request.get_host()+'/accounts/dashboard/'})
                else:
                    return JsonResponse({'redirect':'http://'+request.get_host()+'/accounts/notYet/'})
            else:
                return JsonResponse({'error':'treue'})
        else:
            return JsonResponse({'error':'true'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_i(request):
    logout(request)
    return render(request, 'logout.html', {})

def user_articles(request):
    userr = Article.objects.filter(user=request.user)
    return render(request, 'article_list.html', {'user':userr})