import time
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .forms import UserForm
from .models import SmartPhone, Comments


def about(request):
    return render(request, 'spectra/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['p']
        email = request.POST['q']
        message = request.POST['s']

        send_mail(name, message, email, ['rj203171@gmail.com'], fail_silently=False)
    return render(request, 'spectra/contact.html')


def terms(request):
    return render(request, 'spectra/terms.html')


def privacy(request):
    return render(request, 'spectra/privacy.html')


def index(request):
    return render(request, 'spectra/index.html')


def detail(request):
    name = request.GET['q']
    phone = get_object_or_404(SmartPhone, phone_name=name)
    comments = Comments.objects.all()

    if request.method == 'POST':
        com = Comments()
        com.user = request.user
        com.phone_name = phone.phone_name
        com.datetime = str(time.asctime(time.localtime(time.time())))
        com.comment = request.POST['a']
        com.save()
    return render(request, 'spectra/detail.html', {'phone': phone, 'comments': comments})


def compare1(request, pk):
    phone = get_object_or_404(SmartPhone, pk=pk)
    return render(request, 'spectra/compare.html', {'phone': phone})


def compare2(request):
    return render(request, 'spectra/compare.html')


def comparison(request):
    name1 = request.GET['p']
    name2 = request.GET['q']
    phone1 = get_object_or_404(SmartPhone, phone_name=name1)
    phone2 = get_object_or_404(SmartPhone, phone_name=name2)
    return render(request, 'spectra/comparison.html', {'phone1': phone1, 'phone2': phone2})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'spectra/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'spectra/index.html')
            else:
                return render(request, 'spectra/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'spectra/login.html', {'error_message': 'Invalid login'})
    return render(request, 'spectra/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        try:
            email = form.cleaned_data['email']
            send_mail('Confirmation to Spectra', 'Welcome To Spectra', 'rohan.jagtap@spit.ac.in', [email],
                      fail_silently=False)
        except:
            pass

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'spectra/index.html')
    context = {
        "form": form,
    }
    return render(request, 'spectra/registration_form.html', context)
