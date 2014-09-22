from django.shortcuts import render
from django.http import HttpResponse
from bestplayer.models import Club
def index(request):
    top_five = Club.objects.order_by('name')[:5]
    return render(request,'bestplayer/index.html',{"top_five":top_five})
    
def detail(request,club_id):
    return HttpResponse("her is detail and clubs num is :",club_id )
def result(request,club_id):
    return HttpResponse('her is result that is barraly working ')
def vote (request,club_id):
    return HttpResponse('vote is not in action now')
