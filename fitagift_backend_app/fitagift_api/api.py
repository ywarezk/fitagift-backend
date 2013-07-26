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

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from fitagift_backend_app.models import *

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
    
    class Meta(NerdeezResource.Meta):
        queryset = Question.objects.all()
        
class AnswerResource(NerdeezResource):
    '''
    rest api for the answer model
    '''
    
    class Meta(NerdeezResource.Meta):
        queryset = Answer.objects.all()

#===============================================================================
# end the actual rest api
#===============================================================================
