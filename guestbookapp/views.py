
from django.shortcuts import render_to_response
from models import guests
from django.http import  HttpResponse

# Create your views here.
def home(request):
    return render_to_response('guestbookapp/home.html', {'guests': guests.objects.all()})