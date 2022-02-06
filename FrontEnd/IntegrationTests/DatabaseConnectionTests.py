import unittest
import unittest.mock
import sys
sys.path.append("..")
from databaseconnectionclass import DatabaseConnection
from IntegrationTests.DBBuilder import DBBuilder

class DatabaseConnectionTests(unittest.TestCase):

    def testTestConnection(self):
        connection = DBBuilder.getSQLCheckerConnectionPath()
        result = connection.testConnection()
        self.assertEqual(result,"Connection is valid.")

    def testTestConnectionCanFail(self): # can make a db connection with 5 values (username and password)
        connection = DatabaseConnection("sql",'localhost','waterwork' , 'user', 'pass')
        result = connection.testConnection()
        self.assertEqual(result,"Connection is invalid.")

    def testGetConnectionTrustedCredential(self):
        connection = DBBuilder.getSQLCheckerConnection()
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()