import unittest
import sys
sys.path.append("..")
from difficuiltyclass import Difficulty
from Marks import Marks
from queryclass import Query
from questionclass import Question
from User import User
from IntegrationTests.DBBuilder import DBBuilder


class UserTests(unittest.TestCase):

    user = User('watal385','Alvin Watts')

    def testUserCRUD(self): # Part of DB Integration testing, Order is important.
        connection = DBBuilder.getSQLCheckerConnection()

        self.Create(connection)
        self.Read(connection)
        self.CleanUp(connection)

    def Create(self, connection):
        User.storeUser(connection, self.user)

    def Read(self, connection):
        users = User.getAllUsers(connection)
        
        # 1st read method, get userid from username
        result = User.getIdFromUserName(connection,self.user.UserName)
        self.assertEqual(result, self.user.UserId)

        # 2nd read method, get username by id
        copyUser = User.getUserNameFromId(connection,result)
        self.assertEqual(self.user.UserName,copyUser)
    
    def CleanUp(self, connection):
        DBBuilder.RemoveUser(self,connection,self.user.UserId)
        result = User.getIdFromUserName(connection,self.user.UserName)
        self.assertEqual(result, None)
        

if __name__ == '__main__':
    unittest.main()