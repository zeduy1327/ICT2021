import unittest
import unittest.mock
import uuid
import sys
sys.path.append("..")
from queryclass import Query

class QueryTests(unittest.TestCase):

    def testCanInit3(self): # can make a user with 3 values
        queryId = uuid.uuid1()
        questionId = uuid.uuid1()
        sql = "sql"
        score = 3
        result = Query(questionId, sql, score)
        self.assertEqual(result.questionId, questionId)
        self.assertEqual(result.sql, sql)
        self.assertEqual(result.score,score)

    def testCanInit4(self): # can make a user with 4 values
        queryId = uuid.uuid1()
        questionId = uuid.uuid1()
        sql = "sql"
        score = 3
        result = Query(queryId, questionId, sql, score)
        self.assertEqual(result.questionId, questionId)
        self.assertEqual(result.queryId, queryId)
        self.assertEqual(result.sql, sql)
        self.assertEqual(result.score,score)

    def testCanInit5(self): # can make a user with 5 values
        queryId = uuid.uuid1()
        questionId = uuid.uuid1()
        sql = "sql"
        score = 3
        dataRetrieved = "retrieved"
        timeToExecute = 300
        result = Query(questionId, sql, dataRetrieved, timeToExecute, score)
        self.assertEqual(result.questionId, questionId)
        self.assertEqual(result.sql, sql)
        self.assertEqual(result.dataRetrieved, dataRetrieved)
        self.assertEqual(result.timeToExecute,timeToExecute)
        self.assertEqual(result.score,score)

    # TODO store

if __name__ == '__main__':
    unittest.main()