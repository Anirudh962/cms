from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect,get_object_or_404
from .models import lessonplan
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
  return render(request, 'home.html', {'request': request})

def insertlp(request):
  vlsid = request.POST['lpid'];
  vdescp = request.POST['desc'];
  vcons = request.POST['cosn'];
  lp = lessonplan(lsid=vlsid, descp = vdescp, cosn = vcons);
  lp.save();
  return redirect('viewlessplan')

def viewlessplan(request):
  less = lessonplan.objects.all()
  return render(request,'home.html',{'lessonplan':less})

def deleteprofile(request, id):
  lp = lessonplan.objects.filter(lsid=id)
  lp.delete()
  return redirect('viewlessplan')

def editprofile(request, id):
  lessp = lessonplan.objects.get(lsid=id)
  return render(request,"editprofile.html",{'lessp':lessp})

def updatelessp(request, id):
  newlsid = request.POST['lpid'];
  newdescp = request.POST['desc'];
  newcons = request.POST['cosn'];
  lp = lessonplan.objects.get(lsid=id)
  lp.lsid=newlsid
  lp.descp=newdescp
  lp.cosn=newcons
  lp.save();
  return redirect('viewlessplan')