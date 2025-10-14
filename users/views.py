from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm, LoginForm

# def signup_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect('hub:home')
#     else:
#         form = RegisterForm()
    
#     context = {
#         "form": form,
#     }
    
#     return render(request, "users/sign-up.html", context)

# def signin_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('hub:home')
#         else:
#             print(form.errors)
#     else:
#         form = LoginForm()
        
#     context = {
#         "form": form,
#     }
     
#     return render(request, 'users/sign-in.html', context)

