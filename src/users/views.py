from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import Registrationform, UserUpdateForm, ProfileUpdateForm

def register(request):
    form = Registrationform(request.POST or None)

    if form.is_valid():
        form.save()
        # return redirect("login")

    context = {
        "form":form,
    }
    return render(request, "users/register.html", context)

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect(request.path)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "users/profile.html", context)