from django.shortcuts import render
from .forms import UserRegistrationForm
from authentication.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            fullName = user_form.cleaned_data['first_name'] + \
                ' ' + user_form.cleaned_data['last_name']
            User.objects.create(
                user=new_user, fullname=fullName, allow_login=True)
            return render(request,
                          'register/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'register/register.html',
                  {'user_form': user_form})
