from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Albums
template = loader.get_template('music/index.html')
# Create your views here.
def index(request):
    
    #return HttpResponse("You're looking at question")
    return render(request, 'music/index.html')
def detail(request,album_id):
    all_albums  = Albums.objects.all()

    return HttpResponse(f'Bạn đang xem Album có mã:  {album_id}, tên album là: . Xin cám ơn')
def chitiet(request,album_id):
    all_albums  = Albums.objects.all()
    html = ''
    for list_ in all_albums:
        url = f'/music/{list_.id}/detail'
        html+='<a href=' + url + ">" + list_.album_title + '</a><br>'
    return HttpResponse(html)
    