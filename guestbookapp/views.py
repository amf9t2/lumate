
from django.shortcuts import render_to_response
from guestbookapp.models import guests
from django.http import  HttpResponse
from django.template import Template, Context


def home(request):
    template = Template(
        """Hello, world! Here are all the cities of the world:
        {% for guest in allguest %}
        {
            {guest.last_name}
        }
        {% endfor %}"""
    )
    allguest = guests.objects.all()

    context = Context({"guests": allguest})

    return HttpResponse(template.render(context))
#
# # Create your views here.
# def home(request):
#     return render_to_response('guestbookapp/home.html', {'guests': guests.objects.all()})