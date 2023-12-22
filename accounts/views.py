from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def login_page(request, *args, **kwargs):
    form = AuthenticationForm(request=request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"    
    }
               
    return render(request, "accounts/auth.html", context)

def logout_page(request, *args, **kwargs):
    if (request.method == "POST"):
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "description": "Are you sure you want to log out?",
        "btn_label": "Login",
        "title": "Logout"    
    }
    return render(request, "accounts/auth.html", context)

def register_page(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        return redirect("/")

    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"    
    }
    return render(request, "accounts/auth.html", context)