import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from Marks import Marks

# need to merge master into branch
class MarksTests(unittest.TestCase):
    
    def testCanInit3(self): # can make marks with 3 values
        userid = uuid.uuid1()
        queryid = uuid.uuid1()
        marks = 0
        result = Marks(userid,queryid,marks)
        self.assertEqual(result.userId,userid)
        self.assertEqual(result.queryId,queryid)
        self.assertEqual(result.marks,marks)
   
    def testCanInit4(self): # can make marks with 4 values
        userid = uuid.uuid1()
        queryid = uuid.uuid1()
        marksid = uuid.uuid1()
        marks = 0
        result = Marks(marksid,userid,queryid,marks)
        self.assertEqual(result.userId,userid)
        self.assertEqual(result.queryId,queryid)
        self.assertEqual(result.marks,marks)
        self.assertEqual(result.marksId,marksid)

if __name__ == '__main__':
    
    unittest.main()