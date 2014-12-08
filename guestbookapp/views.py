
from django.shortcuts import render_to_response
from models import guest
from django.http import  HttpResponse

# Create your views here.
def home(request):
    return render_to_response("guestbookapp/home.html", {'guest' : guest.objects.all()})