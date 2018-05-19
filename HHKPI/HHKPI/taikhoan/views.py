from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
template = loader.get_template('taikhoan/login.html')
# Create your views here.
def index(request):
    
    #return HttpResponse("You're looking at question")
    return render(request, 'taikhoan/login.html')