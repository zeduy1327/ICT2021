import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from difficuiltyclass import Difficulty

class DifficuiltyTests(unittest.TestCase):
    
    def testCanInit2(self): # can make a user with 2 values
        result = Difficulty(0,'hero labs')
        self.assertEqual(result.diffLevel,0)
        self.assertEqual(result.description,'hero labs')
    
    def testCanInit3(self): # can make a user with 3 values
        id = str(uuid.uuid1())
        result = Difficulty(id,0,'hero labs')
        self.assertEqual(result.diffLevel,0)
        self.assertEqual(result.description,'hero labs')
        self.assertEqual(result.difficultyId,id)

    # TODO store

if __name__ == '__main__':
    
    unittest.main()