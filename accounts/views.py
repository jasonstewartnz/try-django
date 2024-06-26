from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        

        user = authenticate(request=request, username=username, password=password)

        if user is None:
            context = {"error":"Invalid username or password"}
            return render(request, "accounts/login.html", context=context)

        print(user)

        login(request, user)

        return redirect('/admin')

    return render(request, "accounts/login.html", {})


def logout_view(request):

    if request.method == "POST":
        logout(request)

        return redirect('/login/')
    
    return render(request, "accounts/logout.html", {})

def register_view(request):
    return render(request, "accounts/register.html", {})
