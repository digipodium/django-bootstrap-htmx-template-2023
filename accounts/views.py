from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

# Create your views here.
def login(request):
    ctx = {}
    return render(request, 'accounts/login.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'accounts/register.html', ctx)

def htmx_login(request):
    status = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"testing >>> : {username} {password}")
        if len(username) == 0:
            status = "Username is required"
        elif len(password) == 0:
            status = "Password is required"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                status = "Login successful"
            else:
                status = "Invalid username or password"
    ctx = {'status': status}
    return render(request, 'partials/login_form.html', ctx)

def htmx_register(request):
    ctx = {}
    return render(request, 'partials/register_form.html', ctx)