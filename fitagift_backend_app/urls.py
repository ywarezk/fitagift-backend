'''
our server urls are defined in this page
Created on July 26th, 2013

@author: Yariv Katz
@version: 1.0
@copyright: nerdeez
'''

#===============================================================================
# begin imports
#===============================================================================

from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from fitagift_backend_app.fitagift_api.api import *
import fitagift_backend_app.views
from django.conf.urls import patterns, include, url
from django.contrib import admin

#===============================================================================
# end imports
#===============================================================================

#enable admin
admin.autodiscover()

#register rest urls
v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(AnswerResource())
v1_api.register(FlatpageResource())
v1_api.register(UtilitiesResource())

#register urls
urlpatterns = patterns('',
    # enable admin
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    
    #urls for tastypie
    (r'^api/', include(v1_api.urls)),
    
    #urls for the cross domain comunications
    ('^$', fitagift_backend_app.views.porthole),
    ('^proxy/', fitagift_backend_app.views.proxy),
)
