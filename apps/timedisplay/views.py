from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime(" %B %d , %Y %H:%M  %p" , gmtime())
  }
  return render(request,'timedisplay/page.html', context)

