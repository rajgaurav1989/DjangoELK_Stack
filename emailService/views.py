from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def singleEmail(request) :
	return render_to_response("emailService/singleEmail.html",
                                  {},
                                  context_instance=RequestContext(request))

def bulkEmail(request) :
	return render_to_response("emailService/bulkEmail.html",
                                  {},
                                  context_instance=RequestContext(request))