from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import CreationForm

@login_required
def index(request):
    template = 'users/index.html'
    user = request.user
    contex = {
        'user': user
    }
    return render(request, template, contex)


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = 'users/index.html'
    template_name = 'users/signup.html' 