from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Club,Footballer
from django.core.urlresolvers import reverse
from django.views import generic


"""def index(request):
    top_five = Club.objects.order_by('name')[:5]
    return render(request,'bestplayer/index.html',{"top_five":top_five})
    
def detail(request,club_id):
    club = get_object_or_404(Club,pk = club_id)
    return render(request,'bestplayer/detail.html',{'club':club})
def result(request,club_id):
    club = get_object_or_404(Club,pk = club_id)
    return render(request,'bestplayer/result.html',{'club':club})
"""

class IndexView(generic.ListView):
    template_name = 'bestplayer/index.html'
    context_object_name = 'top_five'
    
    def get_queryset(self):
        return Club.objects.order_by('name')[:5]

class DetailView(generic.DetailView):
    model = Club
    template_name = 'bestplayer/detail.html'
    
class ResultView(generic.DetailView):
    model = Club
    template_name = 'bestplayer/result.html'


def vote (request,club_id):
    club = get_object_or_404(Club,pk = club_id)
    try:
        choosen = club.footballer_set.get(pk = request.POST['klub'])
    except(KeyError, Footballer.DoesNotExist):
        return render(request,'bestplayer/detail.html',{
            'club':club,
            'error_message':"you did not selecte a choice.",
        })
    else:
        choosen.number += 1
        choosen.save()
    
    
    return HttpResponseRedirect(reverse('bestplayer:result', args=(club.id,)))
