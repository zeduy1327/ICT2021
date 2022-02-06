import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from Enrollmet import Enrollment

class EnrollmetTests(unittest.TestCase):
    
    def testCanInit2(self): # can make a user with 2 values
        userid = uuid.uuid1() 
        semesterid = uuid.uuid1()
        result = Enrollment(semesterid, userid)
        self.assertEqual(result.UserId,userid)
        self.assertEqual(result.SemesterId,semesterid)
        
    
    def testCanInit3(self): # can make a user with 3 values, 2 sets of init may not be right.
        userid = uuid.uuid1()
        semesterid = uuid.uuid1() 
        enrollid = uuid.uuid1()

        # init
        result = Enrollment(enrollid, semesterid, userid)

        # Assert
        self.assertEqual(result.EnrollmentId, enrollid)
        self.assertEqual(result.UserId,userid)
        self.assertEqual(result.SemesterId,semesterid)

if __name__ == '__main__':
    
    unittest.main()