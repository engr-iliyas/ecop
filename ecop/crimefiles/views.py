from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

from .forms import ComplaintForm,FirForm,CopStatusForm,CaseStatusForm
from .models import Complaint,Fir,CopStatus,CaseStatus
# Create your views here.


def complaint_create(request):
	form =ComplaintForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
	"form":form
	}
	return render(request,"complaint_form.html",context)

def fir_create(request,id=None):
	if not request.user.groups.filter(name="Police").exists():
		return Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	form =FirForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.complaintid=complaintid
		instance.save()
		messages.success(request,"sucessfully Created")
		return HttpResponseRedirect('/crimefiles/')
	context={
	"form":form
	}
	return render(request,"fir_form.html",context)

def copstatus_create(request,id=None):
	if not request.user.groups.filter(name="Police").exists():
		return Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	form =CopStatusForm(request.POST or None)
	title="Police Procedure"
	if form.is_valid():
		instance=form.save(commit=False)
		instance.complaintid=complaintid
		instance.save()
		messages.success(request,"sucessfully Created")
		return HttpResponseRedirect('/crimefiles/')
	context={
	"title":title,
	"form":form
	}
	return render(request,"CopStatus_form.html",context)

def casestatus_create(request,id=None):
	if not request.user.groups.filter(name="Court").exists():
		return Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	form =CaseStatusForm(request.POST or None)
	title="Case Procedure"
	if form.is_valid():
		instance=form.save(commit=False)
		instance.complaintid=complaintid
		instance.save()
		messages.success(request,"sucessfully Created")
		return HttpResponseRedirect('/crimefiles/')
	context={
	"title":title,
	"form":form
	}
	return render(request,"CopStatus_form.html",context)

def complaint_detail(request,id=None):
	instance=get_object_or_404(Complaint,complaintid=id)
	title2="FIR"
	try:
		instance2=Fir.objects.get(complaintid=id)
	except ObjectDoesNotExist:
		instance2=None
	instance3=CopStatus.objects.filter(complaintid=id)
	instance4=CaseStatus.objects.filter(complaintid=id)
	title3="Police proceeding"
	title4="Case proceeding"
	context={
	"title":instance.complaintid,
	"title2":title2,
	"title3":title3,
	"title4":title4,
	"instance":instance,
	"instance2":instance2,
	"instance3":instance3,
	"instance4":instance4,
	}
	return render(request,"complaint_detail.html",context)

def complaint_list(request):
	# print request.user
	queryset_list=Complaint.objects.all().order_by("-dateofcomplaint")
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	who=request.user
	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context={
	"who":who,
	"object_list":queryset,
	"title":"Complaint lists"
	}
	return render(request,"complaint_list.html",context)

def complaint_update(request,id= None):
	if not request.user.groups.filter(name="citizen").exists():
	 	return Http404
	instance=get_object_or_404(Complaint,complaintid=id)
	form =ComplaintForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"sucessfully updated",extra_tags="xtra")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
	"title":instance.complaintid,
	"instance":instance,
	"form":form,
	}
	return render(request,"complaint_form.html",context)


