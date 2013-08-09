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
        obj = self.deserialize(resp)['objects'][0]
        answers = obj['answers']
        self.assertEqual(len(answers),2)
        
    def test_answer(self):
        '''
        test that the question api is working
        '''
        
        resp = self.api_client.get('/api/v1/answer/', format='json', data={})
        self.assertHttpOK(resp)
        
    def test_flatpage(self):
        '''
        make sure get command works on flatpage url
        '''
        resp = self.api_client.get('/api/v1/flatpage/', format='json', data={})
        self.assertHttpOK(resp)
        
    def test_contactus(self):
        '''
        test send mail
        '''
        resp = self.api_client.post('/api/v1/utilities/contact/', format='json', data={'mail': 'mail', 'message': 'testmessage'})
        self.assertHttpAccepted(resp)
        
    def test_answer_relations(self):
        '''
        test that we return numbers instead of full relationships
        '''
        resp = self.api_client.get('/api/v1/question/', format='json', data={})
        question1 = self.deserialize(resp)['objects'][0]
        self.assertEqual(question1['answers'][0]['goto_question'], 2)
        
#===============================================================================
# end testing
#===============================================================================