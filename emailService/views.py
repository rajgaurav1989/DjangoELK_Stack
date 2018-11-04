from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import thread


@csrf_exempt
@login_required
def singleEmail(request):
	try :	
		if (request.method == 'POST'):
			receiverEmail = request.POST.get('receiverEmail')
			ccEmailIds = [x.strip()
						for x in request.POST.get('ccEmails').split(",")]
			bccEmailIds = [x.strip()
						for x in request.POST.get('bccEmails').split(",")]
			subject = request.POST.get('emailSubject')
			message = request.POST.get('emailBody')
			print receiverEmail+'\t' + \
				str(ccEmailIds)+'\t'+str(bccEmailIds)+'\t'+subject+'\t'+message

			thread.start_new_thread(
				check, (receiverEmail, ccEmailIds, bccEmailIds, subject, message))

			print 'raju main end'
			return render_to_response("emailService/submit.html",
									{},
									context_instance=RequestContext(request))
		else:
			return render_to_response("emailService/singleEmail.html",
									{},
									context_instance=RequestContext(request))
	except Exception as e :
		print 'Exception ',e


@csrf_exempt
@login_required
def bulkEmail(request):
    if (request.method == 'POST'):
        return render_to_response("emailService/submit.html",
                                  {},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response("emailService/bulkEmail.html",
                                  {},
                                  context_instance=RequestContext(request))


def check(receiverEmail, ccEmailIds, bccEmailIds, subject, message):
    a = 1
    print 'raju start '+receiverEmail
    for i in range(100000000):
        a = i + 1
    print 'raju end '+str(a)
