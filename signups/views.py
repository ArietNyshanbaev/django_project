from django.shortcuts import render,render_to_response, RequestContext
from .forms import SignUpForm
from django.contrib import messages


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit = False)
        save_it.save()
        messages.success(request, 'You are cool maaan.')
    return render_to_response('signups/base.html',
                              locals(),
                              context_instance = RequestContext(request))