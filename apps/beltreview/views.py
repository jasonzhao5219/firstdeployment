from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user,book,review
from datetime import datetime
from time import gmtime, strftime

def index(request):
	return render(request,'beltreview/index.html')

def process(request):
	errors = user.objects.basic_validator(request.POST)
	if len(errors):
		print errors
		for error in errors:
			messages.error(request, error)
		return redirect('/')
	else:
		return redirect('/showbook')

def login(request):
	u2=user.objects.filter(email = request.POST['email'],password=request.POST['password'])
	
	
	if len(u2)==1:
		request.session['uid']=u2[0].id
		request.session['name']=u2[0].first_name

		return redirect('/showbook')
	else:
		return redirect('/')


def showbook(request):
	all_book=book.objects.all()
	aa=[]
	for i in range(0,2):
		aa.append(all_book[i])
	all_review=review.objects.all()
	
	context={
		'all_book':aa,
		'all_review':all_review

	}
	
	return render(request,'beltreview/bookshow.html',context)

def add(request):

	return render(request,'add.html')
