import unittest
#from unittest import mock
#import re
#import sys
#from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, tags



class TestPredictSentiment(unittest.TestCase):

    MARKER = "### DO NOT DELETE THIS LINE: beg testing"
    STUDENT = {} # namespace of student code

    @classmethod
    def setUpClass(cls):
        try:
            student_code = open('sentiment_analysis.py','rt').read()
            student_code = student_code.split(cls.MARKER)[0]
        except:
            student_code = ""
        exec(student_code, cls.STUDENT)
        

    @weight(1)
    def test_review1(self):
        """Checking the prediction for a review. (1)"""
        review = "Devoid of any of the qualities that made the first film so special ."
        self.run_test(review, 1.8048500078768488)

    @weight(1)
    def test_review2(self):
        """Checking the prediction for a review. (2)"""
        review = "Ramsay and Morton fill this character study with poetic force and buoyant feeling ."
        self.run_test(review, 2.5286319542312787)

    @weight(1)
    def test_review3(self):
        """Checking the prediction for a review. (3)"""
        review = "A boring , pretentious muddle that uses a sensational , real-life 19th-Century crime as a metaphor for -- well , I 'm not exactly sure what -- and has all the dramatic weight of a raindrop ."
        self.run_test(review, 1.8236213254023188)

    @weight(1)
    def test_review4(self):
        """Checking the prediction for a review. (4)"""
        review = "The Bai brothers have taken an small slice of history and opened it up for all of us to understand , and they 've told a nice little story in the process ."
        self.run_test(review, 2.282023370197764)

        
    def run_test(self, review, score):
        #try:
        dict = TestPredictSentiment.STUDENT['make_word_sentiment_dictionary']("movie_reviews_training.txt")
        predicted = TestPredictSentiment.STUDENT['predict_sentiment_score'](review, dict)
        msg = "\n\nThe review is:"
        msg += "\n"+review
        msg += "\nThe score should be: "+str(score)
        msg += "\nPredicted: "+str(predicted)
        self.assertEqual(round(predicted,3), round(score,3), msg=msg)
        #except:
        #    msg = "\n\nThere was an error when creating or accessing the word sentiment dictionary. "
        #    self.assertTrue(False, msg=msg)

