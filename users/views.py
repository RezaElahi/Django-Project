from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        # case that we submit our information
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}!')
            # now we riderct the user to another page
            return redirect('blog-home')
    else:
        # This is the case when we go to the page and still did not submit anything
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form':form})