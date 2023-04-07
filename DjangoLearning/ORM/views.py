from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import UserCreateForm
from .models import Boock, Catigoris


# Create your views here.
class RegisterUser(CreateView):
    form_class = UserCreateForm
    template_name = 'ORM/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def home(request):
    boock = Boock.objects.all()
    return render(request,'ORM/index.html',{'boock' : boock})
def detail_boock(request, boock_name):
    boock = Boock.objects.get(name=boock_name)
    return render(request, 'ORM/detail_boock.html',{'boock' : boock})
def show_cat(request, cat_id):
    books = Boock.objects.filter(cat_id=cat_id)
    cats = Catigoris.objects.all()
    return render(request, 'ORM/show_cat.html', {'books':books,  'cats':cats})