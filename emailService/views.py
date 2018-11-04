from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
import thread
import smtplib


@csrf_exempt
@login_required
def singleEmail(request):
	try:
		if (request.method == 'POST'):
			sender = request.user.email
			receiverEmail = request.POST.get('receiverEmail')
			ccEmailIds = [x.strip()
						  for x in request.POST.get('ccEmails').split(",")]
			bccEmailIds = [x.strip()
						   for x in request.POST.get('bccEmails').split(",")]
			subject = request.POST.get('emailSubject')
			message = request.POST.get('emailBody')
			print receiverEmail+'\t' + \
				str(ccEmailIds[0])+'\t'+str(bccEmailIds[0]) + \
				'\t'+subject+'\t'+message+'\t'+sender

			thread.start_new_thread(
				check, (sender, receiverEmail, ccEmailIds, bccEmailIds, subject, message))

			print 'raju main end'
			return render_to_response("emailService/submit.html",
									  {},
									  context_instance=RequestContext(request))
		else:
			return render_to_response("emailService/singleEmail.html",
									  {},
									  context_instance=RequestContext(request))
	except Exception as e:
		print 'Exception ', e


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


def check(sender, receiverEmail, ccEmailIds, bccEmailIds, subject, message):
	try:
		ccEmailIds.append(sender)
		payloadMessage = "From: %s\r\n" % sender
		payloadMessage = payloadMessage + "To: %s\r\n" % receiverEmail
		payloadMessage = payloadMessage + "CC: %s\r\n" % ",".join(ccEmailIds)
		payloadMessage = payloadMessage + "Subject: %s\r\n" % subject
		payloadMessage = payloadMessage + "\r\n"
		payloadMessage = payloadMessage + message
		toaddrs = [receiverEmail] + ccEmailIds + bccEmailIds
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, settings.ADMIN_EMAIL_PASSWORD)
		server.set_debuglevel(1)
		server.sendmail(sender, toaddrs, payloadMessage)
		server.quit()
	except :
		print 'Exception'
