from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, UpdateUserForm


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # user.refresh_from_db()
            # # load the profile instance created by the signal
            # user.save()
            # raw_password = form.cleaned_data.get('password1')
            #
            # # login user after signing up
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def user_account(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_account'))
        return redirect(reverse('user_account'))
    else:
        form = UpdateUserForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
    return render(request, 'user_account.html', context={'form': form})
