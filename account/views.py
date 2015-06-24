from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import authenticate

from .models import MyUser

from django.contrib.auth import login as builtin_login
from django.contrib.auth import logout as builtin_logout

from django.template import RequestContext, loader

def usercp(request):
    cntxt = RequestContext(request,{})
    t = loader.get_template('account/usercp.html')
    return HttpResponse(t.render(cntxt));

def register_done(request):
    return HttpResponse("Registration successful, you can now login")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account:usercp'))
    form = UserCreationForm
    return render(request,'account/register.html', {'form':form})

def logout(request):
    builtin_logout(request)
    return HttpResponseRedirect(reverse('account:usercp'))

def login(request):
    """
    Aici habar nu am avut cum sa extind AuthenticationForm`ul (campul de username), si am facut ciobaneasca.
    nici acum nu stiu cum manageuiesc requirementuri, validari, si actiuni din formuri.
    ALSO, i would like some permissions tutorials or something. zici ca is nuca in perete io cu ele.
    """
    ##from pprint import pprint as pp
    ##pp(request.META['QUERY_STRING')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                builtin_login(request, user)
                return HttpResponseRedirect(reverse('account:usercp'))
            else:
                return HttpResponse('Account disabled')
        else:
            return HttpResponse('Invalid login')
    form = AuthenticationForm
    return render(request,'account/login.html', {'form':form})