import unittest
import unittest.mock
import sys
sys.path.append("..")
from databaseconnectionclass import DatabaseConnection

class DatabaseConnectionTests(unittest.TestCase):
    
    def testCanInit4(self): # can make a db connection with 4 values (trusted connection)
        result = DatabaseConnection("sql",'localhost','waterworks' , 'trusted')
        self.assertEqual(result.driver,'sql')
        self.assertEqual(result.serverName,'localhost')
        self.assertEqual(result.databaseName,'waterworks')
        self.assertEqual(result.trustedConnection,'trusted')
    
    def testCanInit5(self): # can make a db connection with 5 values (username and password)
        result = DatabaseConnection("sql",'localhost','waterworks' , 'user', 'pass')
        self.assertEqual(result.driver,'sql')
        self.assertEqual(result.serverName,'localhost')
        self.assertEqual(result.databaseName,'waterworks')
        self.assertEqual(result.serverUsername,'user')
        self.assertEqual(result.serverPassword,'pass')

    def testCanUpdateDatabaseConnection(self): # test database can be updated for connection
        result = DatabaseConnection("sql",'localhost','waterworks' , 'user', 'pass')
        self.assertEqual(result.databaseName,'waterworks')
        result.updateDatabaseConnection('studentDb')
        self.assertEqual(result.databaseName,'studentDb')

    def testCanUpdateServerConnection(self): # test server can be updated for connection
        result = DatabaseConnection("sql",'localhost','waterworks' , 'user', 'pass')
        self.assertEqual(result.serverName,'localhost')
        result.updateServerConnection('192.168.1.101')
        self.assertEqual(result.serverName,'192.168.1.101')

if __name__ == '__main__':
    unittest.main()