from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user,quote
from django.template import RequestContext
from datetime import datetime
from time import gmtime, strftime
import re
REGEX_email=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def index(request):
	

	
	return render(request,'examtwo/index.html')

def process(request):
	if request.method=='POST':
		errors = user.objects.basic_validator(request.POST)
		if len(errors):
			print errors
			for error in errors:
				messages.error(request, error)
			return redirect('/')
		else:
			u3=user.objects.create(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'],birthdate=request.POST['birthdate'])
			
			request.session['uid']=u3.id
			request.session['name']=u3.name
			return redirect('/show')

def login(request):
	if request.method=='POST':
		errors=[]
		error = False
		if len(request.POST['email']) < 1 or len(request.POST['password']) < 1:
			
			errors.append("invalid login email or password")
			error=True
		
		
		if not REGEX_email.match(request.POST['email']):
			errors.append("The login email address is Not a legal one")
			error=True
		for error in errors:
				messages.error(request, error)
		if error:
			return redirect('/')


		
		else:
			u2=user.objects.filter(email = request.POST['email'],password=request.POST['password'])
					
					
			if len(u2)==1:
				request.session['uid']=u2[0].id
						
				request.session['name']=u2[0].name

				return redirect('/show')
			else:
				return redirect('/')


def show(request):
	if request.session['uid']:
		all_user=user.objects.all()
		all_quote1=quote.objects.filter(favorite=0)
		all_quote2=quote.objects.filter(favorite=1)
		
		
		
		context={
			'all_user':all_user,
			'all_quote1':all_quote1,
			'all_quote2': all_quote2
		
		}
		
		return render(request,'examtwo/show.html',context)
	else:
		return redirect('/')

def addquote(request):
	if request.method=='POST':
		errors=[]
		error = False
		if len(request.POST['message']) < 10 or len(request.POST['postby']) < 3:
			
			errors.append(" message length should more than 10  and poster length should more than 3")
			error=True
		
		
		
		for error in errors:
				messages.error(request, error)
		if error:
			return redirect('/show')
		else:
			u1=user.objects.get(name=request.POST['postby'])
			q1=quote.objects.create(message=request.POST['message'],user=u1)
			return redirect('/show')

def addfavorite(request,number):
	if request.method=='POST':
		q1=quote.objects.get(id=number)
		q1.favorite=1
		q1.save()
		return redirect('/show')

def removefavorite(request,number):
	if request.method=='POST':
		q1=quote.objects.get(id=number)
		q1.favorite=0
		q1.save()
		return redirect('/show')

def usersinfo(request,number):
	u1=user.objects.get(id=number)
	request.session['infoname']=u1.name
	q1=user.objects.get(id=number).quotes.all()
	request.session['count']=len(q1)

	return render(request,'examtwo/showone.html',{'infoquote':q1})

def logout(request):
	del request.session['uid']
	return redirect('/')

def dashboard(request):
	return redirect('/show')
	

