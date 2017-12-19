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
	bb=[]
	for i in range(0,3):
		aa.append(all_book[i])

	for i in range(3,len(all_book)):
		bb.append(all_book[i])
	all_review=review.objects.all()
	
	context={
		'firstthree_book':aa,
		'all_review':all_review,
		'other_book':bb
	}
	
	return render(request,'beltreview/bookshow.html',context)

def addbook(request):

	return render(request,'beltreview/bookadd.html')

def logout(request):
	del request.session['uid']
	return redirect('/')

def bookreviewcreate(request):
	print request.POST['new_author']
	if len(request.POST['new_author'])==0:
		b1=book.objects.create(title=request.POST['title'],author=request.POST['author'],rating=request.POST['rating'])
	else:
		b1=book.objects.create(title=request.POST['title'],author=request.POST['new_author'],rating=request.POST['rating'])
	u1=user.objects.get(id=request.session['uid'])
	r1=review.objects.create(review=request.POST['review'],user=u1,book=b1)
	
	u1.books.add(b1)
	
	return redirect('/showone')

def showone(request,number):
	b1=book.objects.get(id=number)
	request.session['showonetitle']=b1.title
	request.session['showoneauthor']=b1.author
	#request.session['showonetime']=b1.reviews.created_at
	#request.session['showonereview']=b1.reviews.review
	return redirect('/showonesuc')

def showonesuc(request):
	return render(request,'beltreview/bookshowone.html')





