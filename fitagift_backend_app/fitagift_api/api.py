'''
Tastypie will play with this file to create a rest server

Created on July 26th, 2013
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez Ltd.
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.resources import ModelResource, ALL
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from fitagift_backend_app.models import *
from django.contrib.auth.models import User
import os
from django.template.loader import get_template
from django.template import Context
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from fitagift_backend_app import settings
from smtplib import SMTPSenderRefused
from tastypie import http
from tastypie.exceptions import ImmediateHttpResponse
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpAccepted,\
    HttpCreated, HttpApplicationError
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.utils import simplejson

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin abstract resources
#===============================================================================

class NerdeezResource(ModelResource):
    '''
    abstract class with commone attribute common to all my rest models
    '''
    
    class Meta:
        allowed_methods = ['get']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        ordering = ['title']

#===============================================================================
# end abstract resources
#===============================================================================

#===============================================================================
# begin the actual rest api
#===============================================================================

class QuestionResource(NerdeezResource):
    '''
    rest api for the question models
    '''
    answers = fields.ToManyField('fitagift_backend_app.fitagift_api.api.AnswerResource', 'answers', full=True, null=True)
    class Meta(NerdeezResource.Meta):
        queryset = Question.objects.all()
        ordering = ['grade']
        
class AnswerResource(NerdeezResource):
    '''
    rest api for the answer model
    '''
    goto_question = fields.ToOneField('fitagift_backend_app.fitagift_api.api.QuestionResource', 'goto_question', full=True, null=True)
    answer_to_question_relevent = fields.ToOneField('fitagift_backend_app.fitagift_api.api.QuestionResource', 'answer_to_question_relevent', full=False, null=True)
    
    class Meta(NerdeezResource.Meta):
        queryset = Answer.objects.all()
        
    def dehydrate(self, bundle):
        '''
        will switch the relations to questions with numbers
        '''
        if 'goto_question' in bundle.data and bundle.data['goto_question'] != None:
            bundle.data['goto_question'] = bundle.data['goto_question']['id']
            
        if 'answer_to_question_relevent' in bundle.data and bundle.data['answer_to_question_relevent'] != None:
            bundle.data['answer_to_question_relevent'] = bundle.data['answer_to_question_relevent']['id']
            
        return bundle
        
class FlatpageResource(NerdeezResource):
    '''
    the rest api for the flatpage
    '''
    class Meta(NerdeezResource.Meta):
        queryset = Flatpage.objects.all()
        filtering = {
                     'title': ALL,
                     }
                     
class UtilitiesResource(NerdeezResource):
    '''
the api for things that are not attached to models:
- contact us: url: /api/v1/utilities/contact/
'''
    
    class Meta(NerdeezResource.Meta):
        allowed_methods = ['post']
      
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/contact%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('contact'), name="api_contact"),
        ]
        
    def contact(self, request=None, **kwargs):
        '''
        will send the message to our mail
        '''
        #get params
        post = simplejson.loads(request.body)
        message = post.get('message')
        mail = post.get('mail')
        admin_mail = os.environ['ADMIN_MAIL']
        
        t = get_template('contact_us_email.html')
        html = t.render(Context({'mail': mail, 'message': message}))
        text_content = strip_tags(html)
        msg = EmailMultiAlternatives(u'Fitagift contact us', text_content, settings.FROM_EMAIL_ADDRESS, [admin_mail])
        msg.attach_alternative(html, "text/html")
        try:
            msg.send()
        except SMTPSenderRefused, e:
            return self.create_response(request, {
                    'success': False,
                    'message': 'Failed to send the email',
                    }, HttpApplicationError )
        
        return self.create_response(request, {
                    'success': True,
                    'message': 'Successfully sent contact message',
                    }, HttpAccepted )

#===============================================================================
# end the actual rest api
#===============================================================================
