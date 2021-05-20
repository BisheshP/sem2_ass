import unittest
import frontend.inventory


class TestFunctions(unittest.TestCase):
    def setUp(self):
        """
            creating a new instance for class Functions
        """
        self.a = frontend.inventory.Functions()

    def test_mergesort(self):
        """
            test if the function results in desired output
        """
        p_id = [8,9,3,7,4]
        self.assertEqual([3,4,7,8,9], self.a.mergesort(p_id) )

    def test_binary_primary(self):
        """
                Function to test if the binary_primary works or not.
        """
        p_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(4, self.a.binary_primary(p_id, 5))

    def tearDown(self):
        """
                function to tear down the frontend.inventory.Functions() reference
        """
        del self.a

class TestInventory(unittest.TestCase):
    def test_add_students(self):
        a = frontend.inventory.Inventory.add_students()




if __name__ == '__main__':
    unittest.main()