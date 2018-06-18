from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    return render(request, 'accounts/sign_up_page.html', {'form':form})

def log_in_page(request):
    return render(request, 'accounts/log_in_page.html', {})

def log_out_page(request):
    return render(request, 'accounts/log_out_page.html', {})