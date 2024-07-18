from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    template_name = 'home.html'
    return render(request,template_name)

@login_required
def home_token(request):
    token = request.GET.get('token')
    print(token)
    if token:
        return render(request, 'home.html')
    else:
        return redirect('/generate_token/')