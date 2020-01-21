from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from .form import UserForm, UserLoginForm
from django.contrib.auth.hashers import (
    PBKDF2PasswordHasher, SHA1PasswordHasher, make_password, check_password
)

# @login_required(None,None , '/login')
def index(request):
    print(request.session['id'])
    return render(request, "index.html")

    # return HttpResponse("Hello, world. You're at the app index.")


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserForm(request.POST)
        user = form.save(commit=False)
        password = make_password(request.POST['password'])
        # if user.is_valid():
        user.set_password(password)
        # user.set_username(request.POST['email'])
        user.save()
        return render(request, "login.html")
    else:
        user = UserForm()
        return render(request, "register.html", {'form': user})


def login_request(request):
    if request.method == 'POST':
        print(check_password('12345', "pbkdf2_sha256$150000$QfLFit0ywde8$ttLgCuPIzIS4wiZNm9OJfE2 + Kr2rLb8W + sXcrcs67Ew ="))
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_result = User.objects.filter(email=email)
        print("They used email: {} and password: {}".format(email, password), user_result.values())

        if user_result:
            print(password,  user_result.values()[0].get('password'))
            is_valid_user = check_password(password, user_result.values()[0].get('password'))
            print(is_valid_user)
            if is_valid_user:
                # user = authenticate(email=email, password=user_result.values()[0].get('password'))
                # print(user)
                #
                # print(user, "Valid User")
                #
                # #     if user.is_active:
                #     login(request, user.values()[0])
                #         return HttpResponseRedirect(reverse('index'))
                # #     else:
                #     return HttpResponse("Your account was inactive.")
                request.session['id'] = user_result.values()[0].get('id')
                return redirect('home')
            else:
                print("Someone tried to login and failed.")
                print("They used email: {} and password: {}".format(email, password))
                return HttpResponse("Invalid login details given")
        else:
            return HttpResponse("Invalid login details given")
    else:
        user = UserLoginForm()
        fields = ['email', 'password']
        return render(request, 'login.html', {'form': user})


def logout(request):
    try:
        del request.session['id']
        return redirect('/login')
    except:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")
    # request.session['id'] = None;
#
# def login(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         user = User.objects.filter(email=request.POST['email'])
#         print(user)
#         if user:
#             # is_valid_user = check_password(user.values()[0].get('password'))
#             # user.password = ch(request.POST['password'])
#             # # if user.is_valid():
#             # user.save()
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {'form': user})
#
#     else:
#         user = UserLoginForm()
#         fields = ['email', 'password']
#         return render(request, "login.html", {'form': user})
