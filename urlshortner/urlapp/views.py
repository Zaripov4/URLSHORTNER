from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import LinkInfo
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    return render(request, 'index.html', {})


def add(request):
    if request.method == 'POST':
        link = request.POST['link']
        short_link = str(uuid.uuid4())[:6]
        new_link = LinkInfo(link=link, short_link=short_link)
        new_link.save()
        return HttpResponse(short_link)


def shorten(request, pk):
    print(request.user)
    print('**************')
    short_link = get_object_or_404(LinkInfo, short_link=pk)
    return redirect(short_link.link)


def my_view(request):
    user_agents = get_user_agent(request)
    if user_agents.is_mobile:
        return "mobile user"
    elif user_agents.is_pc:
        return "Pc user"
