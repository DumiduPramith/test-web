from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_app.models import Search
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request , 'my_app/index.html')

def about(request):
    return render(request, 'my_app/about.html')

def contact(request):
    return render(request, 'my_app/contact.html')

def search(request):
    try:
        user_search = request.GET['search']
        create = Search(search=user_search)
        create.save()
        keywords = {
            'key' : user_search,
        }
        return render(request, 'my_app/results.html',keywords)
    except:
        return redirect('index')