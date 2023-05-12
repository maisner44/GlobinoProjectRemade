from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from users.forms import RangeForm
import random
import time

# def my_view(request):
#     my_number = random.randint(0,20)
#     return render(request, 'dep_choose.html', {'my_number': my_number})
start_time = time.time()
def my_time(request):
    current_time = time.time() - start_time
    context = {'current_time': current_time}
    return render(request, 'my_template.html', context)

def my_view(request):
    if request.method == 'POST':
        form = RangeForm(request.POST)
        if form.is_valid():
            min_value = form.cleaned_data['min_value']
            max_value = form.cleaned_data['max_value']
            random_number = random.randint(min_value, max_value)
            return render(request, 'dep_choose.html', {'form': form, 'random_number': random_number})
    else:
        form = RangeForm()
    return render(request, 'dep_choose.html', {'form': form})



class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name,context)

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = user_name,password = password)
            login(request, user)
            return redirect('dep_choose')
        context = {
            'form': form
        }
        return render(request,self.template_name,context)


