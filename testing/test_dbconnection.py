import unittest
import backend.dbconnection

class TestDBconnect(unittest.TestCase):
    def setUp(self):
        self.obj = backend.dbconnection.DBconnect()

    def test_insert(self):
        query = "insert into inventoryyy values (%s,%s,%s,%s,%s,%s,%s)"
        values = (12001,"Canned Pinto Beans","Pantry",260,500,456,9887659845)
        self.obj.insert(query, values)
        query1 = "select * from inventoryyy where id=12001"
        actual = self.obj.select2(query1)
        print(actual)
        self.assertEqual(values, actual[0])

    def test_update(self):
        query = "insert into inventoryyy values (%s,%s,%s,%s,%s,%s,%s)"
        values = (99777, "Canned Pinto Beans", "Pantry", 260, 500, 456, 9887659845)
        self.obj.insert(query, values)
        query1 = "update inventoryyy set name=%s where id=%s"
        values1 = ("Kra",99777)
        self.obj.update(query1,values1)
        query2 = "select * from inventoryyy where id=99777"
        actual = self.obj.select(query2)
        self.assertEqual((99777, "Kra", "Pantry", 260, 500, 456, 9887659845), actual[0])

if __name__ == '__main__':
    unittest.main()
