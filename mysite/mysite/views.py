import os

from twilio.rest import Client

from django import forms
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from captcha.fields import CaptchaField

# Twilio client
client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH)


def index(request):
    context = {
        "form": ContactMeForm(),
        "download_resume_form": DownloadResumeForm(),
    }
    return render(request, 'mysite/index.html', context)


def demo(request):
    return render(request, 'mysite/demo.html')


def contact_me(request):
    if request.method == 'POST':

        form = ContactMeForm(request.POST)

        if form.is_valid():

            try:
                message = client.messages.create(
                    body=f"{ form.cleaned_data['message'] } from { form.cleaned_data['phone'] }/{ form.cleaned_data['email'] }",
                    from_=settings.TWILIO_PHONE,
                    to='+16467700783'
                )

                messages.add_message(request, messages.SUCCESS, 'Your message was sent.')


            except Exception as e:
                messages.add_message(request, messages.ERROR, 'Your message was not sent.', extra_tags="danger")
                pass

        else:
            if form.errors['captcha'] != None:
                messages.add_message(request, messages.ERROR, form.errors['captcha'][0], extra_tags="danger")
            else:
                messages.add_message(request, messages.ERROR, 'Your message was not sent.', extra_tags="danger")


    return redirect(reverse_lazy('index'))

def download_resume(request):

    if request.method == 'POST':

        form = DownloadResumeForm(request.POST)
        if form.is_valid():

            try:
                message = client.messages.create(
                    body=f"{ form.cleaned_data['phone'] }/{ form.cleaned_data['email'] } downloaded your resume",
                    from_=settings.TWILIO_PHONE,
                    to='+16467700783'
                )

                resume_file_path = os.path.join(settings.BASE_DIR, 'mysite/static/mysite/resume/20201021_resume_maverick_moore.docx')

                with open(resume_file_path, 'rb') as f:
                    file_data = f.read()

                   # sending response
                response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename="maverick_moore_resume.docx"'

                return response

            except Exception as e:
                messages.add_message(request, messages.ERROR, 'There was an error', extra_tags="danger")
                pass

        else:
            if form.errors['captcha'] != None:
                messages.add_message(request, messages.ERROR, form.errors['captcha'][0], extra_tags="danger")
            else:
                messages.add_message(request, messages.ERROR, 'There was an error.', extra_tags="danger")

    return redirect(reverse_lazy('index'))


class ContactMeForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()


class DownloadResumeForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()
    captcha = CaptchaField()
