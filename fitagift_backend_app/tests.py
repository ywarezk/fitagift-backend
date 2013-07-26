'''
For my TDD, bitch

Created on July 26th, 2013

@author: ywarezk
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.test import ResourceTestCase

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin testing
#===============================================================================

class ApiTest(ResourceTestCase):
    '''
    nerdeez backend tests will be written here
    '''
    fixtures = ['fitagift_backend_app']
    
    def test_question(self):
        '''
        test that the question api is working
        '''
        
        resp = self.api_client.get('/api/v1/question/', format='json', data={})
        self.assertHttpOK(resp)
        
    def test_answer(self):
        '''
        test that the question api is working
        '''
        
        resp = self.api_client.get('/api/v1/answer/', format='json', data={})
        self.assertHttpOK(resp)
        
#===============================================================================
# end testing
#===============================================================================