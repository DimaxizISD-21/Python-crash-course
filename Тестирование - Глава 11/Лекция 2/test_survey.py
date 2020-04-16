import unittest
from survey import AnonymousSurvey

# обычный тест

#class TestAnonymousSurvey(unittest.TestCase):
#     def test_store_single_response(self):
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')

#         self.assertIn('English', my_survey.responses)

#     def test_store_three_response(self):
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Greek', 'Spanish']
        
#         for response in responses:
#             my_survey.store_response(response)

#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# unittest.main()

##############################################################
# тест с использованием метода setUp, который находится в TestCase

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Greek', 'Spanish']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()