from django.shortcuts import render, redirect
from app.forms import UserForm
from app.models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    all = User.objects.all()
    paginator = Paginator(all, 9)
    pages = request.GET.get('page')

    search = request.GET.get('search')
    if search:
        data['db'] = User.objects.filter(username__icontains = search)
    else:
        data['db'] = paginator.get_page(pages)

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = UserForm()
    return render(request, 'form.html', data)

def create(request):
    form =  UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = User.objects.get(pk = pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = User.objects.get(pk = pk)
    data['form'] = UserForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = User.objects.get(pk = pk)
    form = UserForm(request.POST, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = User.objects.get(pk = pk)
    db.delete()
    return redirect('home')
