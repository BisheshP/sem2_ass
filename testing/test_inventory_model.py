import unittest
import model.inventory_model

class TestInventory_m(unittest.TestCase):
    def setUp(self):
        """
            creating a new instance for class Inventory_m
        """
        self.a = model.inventory_model.Inventory_m()
    def test_set_id(self):
        #Assume
        id=1
        #Action
        result = self.a.set_id(id)
        #Assert
        self.assertEqual(1, self.a.get_id())
    def test_set_qty(self):
        #Assume
        qty = 58
        #Action
        result = self.a.set_qty(qty)
        #Assert
        self.assertEqual(58, self.a.get_qty())
    def tearDown(self):
        """
                function to tear down the object
        """
        del self.a

if __name__ == '__main__':
    unittest.main()