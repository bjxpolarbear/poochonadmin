from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .forms import UserForm

# Create your views here.

class UserFormView(View):

    form_class = UserForm
    template_name = 'users/registration.html'


    # display a blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, context={'form':form})


    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request,user)
                    return redirect('home:index')

        return render(request, self.template_name, context={'form':form})

'''
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    redirect_field_name = 'home:index'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def get_success_url(self):

        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.redirect_field_name
        return redirect_to


    # display a blank form
    def get(self,request, *args, **kwargs):
        return super(LoginFormView, self).get(request, *args, **kwargs)


    # process form data
    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            login(self.request, form.get_user())
            return redirect('home:index')

        else:
            return redirect('users:login')
'''