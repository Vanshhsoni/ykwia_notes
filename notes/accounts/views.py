from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from paper.views import home
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def auth_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Correct credentials, log in
            login(request, user)
            return redirect('paper:home')
        else:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Incorrect password for existing account")
                return redirect('accounts:auth')  # redirect back to login page
            else:
                # Create new user if username doesn't exist
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('paper:home')
                
    return render(request, 'accounts/auth.html')

    
def logout_view(request):
    logout(request)
    return redirect('landing')

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out the user first
        user.delete()    # Delete the account
        messages.success(request, "Your account has been deleted permanently.")
        return redirect('paper:home')  # Or redirect to landing page
    return redirect('paper:home')

