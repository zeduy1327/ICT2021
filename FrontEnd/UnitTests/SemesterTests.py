import unittest
import unittest.mock as mock
import datetime
import sys
import pyodbc
import uuid
sys.path.append("..")
from Semester import Semester

class SemesterTests(unittest.TestCase):
    
    def testCanInit5(self):
        newSemester = Semester(2,2021,datetime.date(2021,3,1),datetime.date(2021,7,1),'code')
        self.assertEqual(newSemester.studyPeriod, 2)
        self.assertEqual(newSemester.year, 2021)
        self.assertEqual(newSemester.startDate, datetime.date(2021,3,1))
        self.assertEqual(newSemester.endDate, datetime.date(2021,7,1))
        self.assertEqual(newSemester.code, 'code')

    def testCanInit6(self):
        semesterId = str(uuid.uuid1())
        newSemester = Semester(semesterId,2,2021,datetime.date(2021,3,1),datetime.date(2021,7,1),'code')
        self.assertEqual(newSemester.studyPeriod, 2)
        self.assertEqual(newSemester.year, 2021)
        self.assertEqual(newSemester.startDate, datetime.date(2021,3,1))
        self.assertEqual(newSemester.endDate, datetime.date(2021,7,1))
        self.assertEqual(newSemester.code, 'code')
        self.assertEqual(newSemester.semesterId, semesterId)

if __name__ == '__main__':
    unittest.main()