#! -*- coding=utf8 -*-
"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



class BootstrapForm(forms.Form):
    exclude_bootstrap=[]
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not field in self.exclude_bootstrap:
                self.fields[field].widget.attrs.update({'class' : 'form-control'})
                self.fields[field].widget.attrs.update({'placeholder' : self.fields[field].label})



class ContactForm(BootstrapForm):
    name = forms.CharField(label=u"Имя")
    phone = forms.CharField(label=u"Телефон")
    email = forms.CharField(label="e-mail")
    message = forms.CharField(widget=forms.Textarea,required=False,label=u"Вопрос")

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        plaintext = get_template('mail_detail.html')
        b= {'name':self.cleaned_data['name'],
            'phone':self.cleaned_data['phone'],
            'email':self.cleaned_data['email'],
            'text':self.cleaned_data['message']}
        message_body = plaintext.render(b)
        email = EmailMultiAlternatives('Пришла заявка с сайта kovka-59.ru',
                         message_body,
                         to=['che-email@yandex.ru',
                             'mr.levdanilov@mail.ru',
                             ])
        email.attach_alternative(message_body, "text/html")

        a=email.send()
        print(a)

