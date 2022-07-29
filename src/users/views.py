from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import Registrationform

def register(request):
    form = Registrationform(request.POST or None)

    if form.is_valid():
        form.save()
        # return redirect("login")

    context = {
        "form":form,
    }
    return render(request, "users/register.html", context)
