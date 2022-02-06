import unittest
import sys
import datetime
sys.path.append("..")
from Semester import Semester
from IntegrationTests.DBBuilder import DBBuilder

class SemesterTests(unittest.TestCase):

    def testCanStoreAndGetCurrentSemester(self):
        # Variables
        semester = Semester(2,'2021',datetime.date(2021,3,1),datetime.date(2021,7,1),'INFS2022')
        connection = DBBuilder.getSQLCheckerConnection()
        
        # Store
        semester.storeSemester(connection)
        
        # Retrieve and Check
        result = Semester.getCurrentSemester(connection)
        self.assertEqual(result.semesterId,semester.semesterId)       
        self.assertEqual(result.studyPeriod,semester.studyPeriod)
        self.assertEqual(result.year,semester.year)
        self.assertEqual(result.startDate,semester.startDate)
        self.assertEqual(result.endDate,semester.endDate)
        self.assertEqual(result.code,semester.code)

        # Cleanup
        DBBuilder.RemoveSemester(self,connection,semester.semesterId)

if __name__ == '__main__':
    unittest.main()