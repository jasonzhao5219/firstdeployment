from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user,travel
from django.template import RequestContext
from datetime import datetime
from time import gmtime, strftime
def index(request):
	

	
	return render(request,'djangoexam/index.html')

def process(request):
	errors = user.objects.basic_validator(request.POST)
	if len(errors):
		print errors
		for error in errors:
			messages.error(request, error)
		return redirect('/')
	else:
		u3=user.objects.create(name=request.POST['name'],user_name=request.POST['username'],password=request.POST['password'])
		
		request.session['uid']=u3.id
		request.session['name']=u3.user_name
		return redirect('/show')

def login(request):
	u2=user.objects.filter(user_name = request.POST['username'],password=request.POST['password'])
	
	
	if len(u2)==1:
		request.session['uid']=u2[0].id
		
		request.session['name']=u2[0].user_name

		return redirect('/show')
	else:
		return redirect('/')


def show(request):
	if request.session['uid']:
		all_travel=travel.objects.all()
		all_user=user.objects.all()
		ushow=user.objects.get(id=request.session['uid']).travels.all()
		all_uother=user.objects.exclude(id=request.session['uid'])
		
		arr1=[]
		for i in all_uother:
			arr1.append(i.travels.all())
		
		context={
			'all_user':all_user,
			'all_travel':all_travel,
			'ushow':ushow,
			'uother':arr1
		}
		
		return render(request,'djangoexam/show.html',context)
	else:
		return redirect('/')

def add(request):
	return render(request,'djangoexam/add.html')


	
def addsuc(request):
	if request.method=="POST":
		if request.session['uid']:
			errors = travel.objects.basic_validator(request.POST)

			if len(errors):
				print errors
				for error in errors:
					messages.error(request, error)
				return redirect('/add')
			else:
				t1=travel.objects.create(destination=request.POST['d1'],description=request.POST['description'],start_date=request.POST['startdate'],end_date=request.POST['enddate'])
				u1=user.objects.get(id=request.session['uid'])
				u1.travels.add(t1)
				request.session['planner']=request.session['name']
				return redirect('/show')
		else:
			return redirect('/')
	
	
def destination(request,number):
	request.session['tid']=number
	t22=travel.objects.get(id=number)
	request.session['tname']=t22.destination
	request.session['tdescription']=t22.description
	time1=t22.start_date
	time1=datetime.timetuple(time1)
	request.session['tstart']= str(strftime("%Y %m %d ",time1))
	
	time2=t22.end_date
	time2=datetime.timetuple(time2)
	request.session['tend']= str(strftime("%Y %m %d ",time2))


	
	return redirect('/dsuc')

def dsuc(request):
	others=travel.objects.get(id=request.session['tid']).users.all()
	others2=others.exclude(user_name=request.session['planner'])
	return render(request,'djangoexam/showone.html',{'other':others2})


def logout(request):
	del request.session['uid']
	return redirect('/')
	
def join(request,number):
	u1=user.objects.get(id=request.session['uid'])
	t1=travel.objects.get(id=number)
	u1.travels.add(t1)
	return redirect('/show')