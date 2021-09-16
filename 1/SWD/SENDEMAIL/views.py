from django.shortcuts import render
from SWD.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def send(request):
    mail = forms.Sendmail()
    if request.method == 'POST':
        mail = forms.Sendmail(request.POST)
        subject = 'TESTSWD'
        message = str(mail['Message'].value())
        #print(message)
        recepient = str(mail['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER,[recepient], fail_silently=False)

        context = {
            'message':message,
            'recepient':recepient
        }
        #return render(request, 'sendsucess.html', context)
        messages.info(request,'send succesfully')
    return render(request, 'sendemail/index.html', {'form':mail}) 
