import unittest
import uuid
import sys
sys.path.append("..")
from deductionclass import Deduction

class DifficuiltyTests(unittest.TestCase):
    
    def testCanInit4(self): # can make a user with 3 values
        result = Deduction("queryId",'description','feedback' , 2.0)
        self.assertEqual(result.queryId,"queryId")
        self.assertEqual(result.description,'description')
        self.assertEqual(result.feedback,'feedback')
        self.assertEqual(result.deductionValue, 2.0)
    
    def testCanInit5(self): # can make a user with 5 values
        id = str(uuid.uuid1())
        result = Deduction(id,"queryId",'description','feedback',2.0)
        self.assertEqual(result.queryId,"queryId")
        self.assertEqual(result.description,'description')
        self.assertEqual(result.deductionValue, 2.0)
        self.assertEqual(result.feedback,'feedback')
        self.assertEqual(result.deductionId, id)

    # TODO store

if __name__ == '__main__':
    print('run tests')
    unittest.main()