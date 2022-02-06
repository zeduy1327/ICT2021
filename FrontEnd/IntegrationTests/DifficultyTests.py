import unittest
import sys
import datetime
sys.path.append("..")
from difficuiltyclass import Difficulty
from IntegrationTests.DBBuilder import DBBuilder

class SemesterTests(unittest.TestCase):

    def testDifficultyIntegration(self):
        # Variables
        difficulty = Difficulty(0,'hero labs')
        connection = DBBuilder.getSQLCheckerConnection()
        
        # Store
        difficulty.storeDifficulty(connection)
        
        # Retrieve and Check
        result = Difficulty.getDifficultyId(difficulty.diffLevel,connection)
        self.assertEqual(difficulty.difficultyId,result)
        
        result = Difficulty.getDifficultyFromId(result,connection)
        self.assertEqual(result.description, difficulty.description)     
        self.assertEqual(result.difficultyId, difficulty.difficultyId)
        self.assertEqual(result.diffLevel, difficulty.diffLevel)

        # Cleanup
        DBBuilder.RemoveDifficulty(self,connection,difficulty.difficultyId)

if __name__ == '__main__':
    unittest.main()