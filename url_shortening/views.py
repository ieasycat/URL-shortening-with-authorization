from django.contrib.auth import logout, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from url_shortening.forms import URLForm, RegisterUserForm, LoginUserForm
from url_shortening.models import URL
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


def index(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def profile(request):
    urls_list = URL.objects.filter(user=request.user).all()
    paginator = Paginator(urls_list[::-1], 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.POST:
        form = URLForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = cd.get('url')
            URL.objects.create(
                url=url,
                user=request.user
            )
            return redirect('profile')
    else:
        form = URLForm()

    context = {
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'profile.html', context=context)


def redirect_original(request, url_id: str):
    if request.method == 'GET':
        short_url = get_object_or_404(URL, pk=url_id)
        return redirect(short_url.url)
