from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login user
            login(request, user)
            return redirect('mainApp:view_page')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up_page.html', {'form':form})

@csrf_exempt
def log_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('mainApp:view_page')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/log_in_page.html', {'form':form})

@csrf_exempt
def log_out_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('mainApp:view_page')
    return render(request, 'accounts/log_out_page.html', {})