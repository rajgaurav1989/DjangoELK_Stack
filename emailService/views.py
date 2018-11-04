from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def singleEmail(request) :
	return HttpResponse("Hello, world. Single Email")

def bulkEmail(request) :
	return HttpResponse("Hello, world. Bulk Email")