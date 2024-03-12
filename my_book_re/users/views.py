import re
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


from users.forms import UserLoginForm, UserRecipeForm, UserRegistrationForm, UserProfileForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, добро пожаловать!")
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout')
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()        
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегестрированы!")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, " Ваш профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {
        'title': 'Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, спасибо что были с нами, возвращайтесь скорее!")
    auth.logout(request)
    return redirect(reverse('main:index'))



def add_recipe(request):
    user = request.user
  
    if request.method == 'POST':
        form = UserRecipeForm(data=request.POST,  files= request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш рецепт успешно добавлен")
            return HttpResponseRedirect(reverse('main:index'))      
    else:
        form = UserRecipeForm()
    
    context = {
        'title':'Добавление рецепта',
        'user': user,
        'form': form
    }
    return render(request,'users/user_add_recipe.html', context)




  
    


        



        
    
    
