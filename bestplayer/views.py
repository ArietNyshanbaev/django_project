from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from bestplayer.models import Club
from django.core.urlresolvers import reverse
def index(request):
    top_five = Club.objects.order_by('name')[:5]
    return render(request,'bestplayer/index.html',{"top_five":top_five})
    
def detail(request,club_id):
    club = get_object_or_404(Club,pk = club_id)
    return render(request,'bestplayer/detail.html',{'club':club})
def result(request,club_id):
    return HttpResponse('congrats u have just voted')
def vote (request,club_id):
    club = get_object_or_404(Club,pk = club_id)
    return HttpResponseRedirect(reverse('bestplayer:result', args=(club.id,)))
