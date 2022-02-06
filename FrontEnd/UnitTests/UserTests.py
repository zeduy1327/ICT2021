import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from User import User

class UserTests(unittest.TestCase):
    
    def testCanInit2(self): # can make a user with 2 values
        testUser = User('hero labs','herol012')
        self.assertEqual(testUser.UserName,'herol012')
        self.assertEqual(testUser.FullName,'hero labs')
    
    def testCanInit3(self): # can make a user with 3 values
        userid = uuid.uuid1() 
        testUser = User(userid,'hero labs','herol012')
        self.assertEqual(testUser.UserId, userid)
        self.assertEqual(testUser.UserName,'herol012')
        self.assertEqual(testUser.FullName,'hero labs')

    # TODO
    def testCanStoreUser(self): # can store a user in a db
        userid = uuid.uuid1()
        testUser = User(userid,'herol012','hero labs')
    
    def testCanRetrieveUser(self):
        userid = uuid.uuid1() # user id

if __name__ == '__main__':
    unittest.main()