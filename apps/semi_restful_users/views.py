from django.shortcuts import render, HttpResponse, redirect
from .models import users
from datetime import datetime
from time import gmtime, strftime

def index(request):
	all_users=users.objects.all()
	#print all_users
	context={
		'all_users':all_users
	}
	return render(request,"index.html",context)


def show(request,number):
	request.session['number']=number
	u=users.objects.get(id=number)
	request.session['uid']=number
	request.session['name']=u.first_name
	request.session['last_name']=u.last_name
	request.session['email']=u.email
	time=u.created_at
	time=datetime.timetuple(time)
	request.session['create']= str(strftime("%Y %m %d ",time))
	#request.session['create']=strftime(u.created_at)

	return render(request,"show.html")

def new(request):
	return render(request,"add.html")

def create(request):
	if request.method == "POST":

		u1=users.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'])
		
		print u1.first_name
		return redirect('/users/new')

	else:
		return redirect('/users')

def edit(request,number):
	request.session['number']=number
	u=users.objects.get(id=number)

	request.session['name']=u.first_name
	request.session['last_name']=u.last_name
	request.session['email']=u.email
	print u.id
	request.session['uid']=u.id

	return render(request,"edit.html",{'user':u})

def update(request,number):
	if request.method == "POST":

		u=users.objects.get(id=number)
		u.first_name=request.POST['firstname']
		u.last_name=request.POST['lastname']
		u.email=request.POST['email']
		u.save()
		
		
		return redirect('/users')

	else:
		return redirect('/users')

def destroy(request,number):
	u=users.objects.get(id=number)
	u.delete()
	return redirect('/users')




