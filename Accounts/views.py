from django.shortcuts import  render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from Planner.models import User_Interaction_Details
from datetime import datetime
# to make sense of and use user details.
# in sync with the planner object.

USD = User_Interaction_Details

def Sign_In(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            username = form.cleaned_data.get('username')

            # Updating the user's first login details.
            row = User_Interaction_Details.objects.create(Username=username, LLogin=datetime.now().replace(microsecond=0),
                                                                 LInteract=datetime.now().replace(microsecond=0))


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

                objects = User_Interaction_Details.objects.get(Username=username)
                objects.LLogin, objects.LInteraction = datetime.now().replace(microsecond=0), datetime.now().replace(microsecond=0)
                # Updating the user's last login details.
                objects.save()

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
