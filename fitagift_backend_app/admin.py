'''
will hold the admin interface models

Created on July 22, 2013
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez Ltd
'''

#===============================================================================
# begin imports
#===============================================================================

from django.contrib import admin
from fitagift_backend_app.models import *
from django.contrib import admin

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin admin models
#===============================================================================

class QuestionAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

class FlatpageAdmin(admin.ModelAdmin):
    pass


#===============================================================================
# end admin models
#===============================================================================

#===============================================================================
# begin admin site regitration
#===============================================================================

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Flatpage, FlatpageAdmin)


#===============================================================================
# end admin site registration
#===============================================================================