from django.shortcuts import  render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def Sign_In(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/Homepage/")

        else:
            print(form.errors)

        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomUserForm()
    return render(request=request, template_name="Sign_Up.html", context={"register_form":form})

def Log_In(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/Homepage/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="Log_In.html", context={"login_form": form})

def Log_Out(request):
    logout(request)
    return redirect('/Login/')

def redirect_to_log_in(request):
    return redirect('Login/')

# Create your views here.
