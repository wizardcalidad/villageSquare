from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from profiles.models import Profile
from register.forms import LoginForm


#
# def register(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password1']
#         password_reset = request.POST['password2']
#
#         if password == password_reset:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'username already exist')
#                 return render(request, 'register/register.html')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'email already taken')
#                 return render(request, 'register/register.html')
#             else:
#                 user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
#                                                 email=email, password=password)
#                 user.save()
#                 Profile.user = user
#                 return redirect('register:signup')
#         else:
#             messages.info(request, 'password does not match')
#             return render(request, 'register/register.html')
#     else:
#         return render(request, 'register/register.html')
#
# #
# # def user_login(request):
# #     if request.method == 'POST':
# #         form = LoginForm(request.POST)
# #         if form.is_valid():
# #             cd = form.cleaned_data
# #             user = authenticate(request,
# #                                 username=cd['username'],
# #                                 password=cd['password'])
# #             if user is not None:
# #                 if user.is_active:
# #                     login(request, user)
# #                     return HttpResponse('Authenticated', 'successfully')
# #                 else:
# #                     return HttpResponse('Disabled account')
# #             else:
# #                 return HttpResponse('Invalid login')
# #         else:
# #             form = LoginForm()
# #         return render(request, 'register/login.html', {'form': form})
# #     else:
# #         return render(request, 'register/login.html')
#
#
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register/register.html'
