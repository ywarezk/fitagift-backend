'''
Backend models/tables will be defined here

Created on July 22nd 2013
@author: Yariv Katz
@copyright: nerdeez Ltd.
@version: 1.0
'''

#==========================================
# begin imports
#==========================================

from django.db import models
from django.contrib.contenttypes.models import ContentType
import datetime

#==========================================
# end imports
#==========================================


#===============================================================================
# begin constants
#===============================================================================

QUESTION_TYPE_CHOICES = (
                   (1, 'Buttons'),
                   (2, 'Combobox'),
                   (3, 'Textfield'),
                   (4, 'Textfield completion')
                   )

DEFAULT_QUESTION_TYPE_CHOICE = 1


#===============================================================================
# end constants
#===============================================================================

#==========================================
# begin abstact models
#==========================================

class NerdeezModel(models.Model):
    '''
    this class will be an abstract class for all my models
    and it will contain common information
    '''
    
    creation_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0))
    modified_data = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0), auto_now=True)
    
    class Meta:
        abstract = True
        
#==========================================
# end abstact models
#==========================================


#==========================================
# begin models
#==========================================

class Question(NerdeezModel):
    '''
    represents a question
    '''
    title = models.CharField(max_length=300, blank=False, null=False, default='')
    text = models.TextField(blank=False, null=False)
    grade = models.IntegerField(default=0)
    question_type = models.IntegerField(choices = QUESTION_TYPE_CHOICES, default = DEFAULT_QUESTION_TYPE_CHOICE, blank=False, null=False)
    def __unicode__(self):
        return self.title
    
class Answer(NerdeezModel):
    '''
    answer to a question
    '''
    title = models.CharField(max_length=1000, blank=False, null=False)
    goto_question = models.ForeignKey(Question, related_name='next_question', blank=True, null=True, default=None)
    belong_to_question = models.ForeignKey(Question, related_name='answers', blank=True, null=True, default=None)
    answer_to_question_relevent = models.ForeignKey(Question, related_name='relevent_question', blank=True, null=True, default=None)
    words = models.CharField(max_length=300, blank=True, null=True, default=None)
    query_relevent_question = models.CharField(max_length=500, blank=True, null=True, default=None)
    icon_class = models.CharField(max_length=100, blank=True , null=True, default=None)
    is_other = models.BooleanField(default=False)
    placeholder = models.CharField(max_length=200, default=None, blank=True, null=True)
    grade = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
        
class Flatpage(NerdeezModel):
    '''
    the flatpage table
    '''
    title = models.CharField(max_length=250, blank=False, null=False, unique=True)
    html = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
    

#==========================================
# end models
#==========================================