from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from users.forms import RegisterForm, LoginForm
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class RegisterView(APIView):
    """
    A ViewSet for registering users.
    """
    
    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

















































































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