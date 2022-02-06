import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from questionclass import Question

class QuestionTests(unittest.TestCase):

    def testCanInit3(self): # can make a user with 3 values
        questionId = str(uuid.uuid1())
        question = 'what is the average velocity of a laiden swallow?'
        difficultyId = str(uuid.uuid1())
        result = Question(questionId, question, difficultyId)
        self.assertEqual(result.questionId,questionId)
        self.assertEqual(result.question,question)
        self.assertEqual(result.difficultyId,difficultyId)
    
    def testCanInit2(self): # can make a user with 2 values
        question = 'what is the average velocity of a laiden swallow?'
        difficultyId = str(uuid.uuid1())
        result = Question(question, difficultyId)
        self.assertEqual(result.question,question)
        self.assertEqual(result.difficultyId,difficultyId)

    # TODO store

if __name__ == '__main__':
    unittest.main()