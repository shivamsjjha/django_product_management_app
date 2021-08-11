from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Body,TurorialCategory,TurorialSeries,Turorial
from math import ceil
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.models import User, auth

# Create your views here.
def single_slug(request, single_slug):
	categories = [c.category_slug for c in TurorialCategory.objects.all()]
	if single_slug in categories:
		matching_series = TurorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
		series_urls={}
		for m in matching_series.all():
			part_one = Turorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("published")
			series_urls[m]= part_one.tutorial_slug
		return render(request,'category.html',{'part_one':series_urls})
	tutorials = [t.tutorial_slug for t in Turorial.objects.all()]
	if single_slug in tutorials:
		this_tutorial = Turorial.objects.get(tutorial_slug=single_slug)
		tutorials_from_series = Turorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("published")
		return render(request,'tutorials.html',{'context': tutorials_from_series})
	return HttpResponse(f"{single_slug} does not correspond to anything.")




@login_required
def gallery(request):
	return render(request,'gallery.html',context={'categories':TurorialCategory.objects.all()})







def header(request):
	return render(request,'header.html')

def signup(request):
	if(request.method=='POST'):
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('/signup')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('/signup')
			else:
				user=User.objects.create_user(username=username, password=password1,email=email)
				user.save();
				print('user created')
				return redirect('/home')
		else:
			messages.info(request,'password not matching')
			return redirect('/signup')
		return redirect('/home')
	else:
		return render(request,'signup.html')


def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user= auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/home')
		else:
			print('invalid')
			messages.info(request,'Enter Correct  combination of Username and password')
			return redirect('/')
	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')


@login_required
def home(request):
	context2=Body.objects.all()
	return render(request,'home.html',{'context2':context2})


@login_required		
def about(request):
	return render(request,'about.html')



@login_required
def contact(request):
	 form = ContactForm()
	 if request.method=='POST':
	 	form = ContactForm(request.POST)
	 	if form.is_valid():
	 		email=form.cleaned_data.get('email')
	 		subject=form.cleaned_data.get('subject')
	 		message=form.cleaned_data.get('message')
	 		sendmail=send_mail(subject,message,email,['shivamjha320@gmail.com'])
	 		print(sendmail)
	 return render(request,'contact.html',{'form':form})
