from django.shortcuts import render, HttpResponse, redirect

from django.utils.crypto import get_random_string
def index(request):

	request.session['aa']+=1
	context={"randomstring":get_random_string(length=14)}
	return render(request,"randomword/index.html",context)
def reset(request):
	request.session['aa']=0
	return redirect('/')

