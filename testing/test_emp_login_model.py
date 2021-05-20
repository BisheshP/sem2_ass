import unittest
import model.emp_login_model

class TestEmp_info(unittest.TestCase):
    def setUp(self):
        """
            creating a new instance for class Functions
        """
        self.a = model.emp_login_model.Emp_info()
    def test_set_fname(self):
        #Assume
        fname = "Bishesh"
        #Action
        result = self.a.set_fname("Bishesh")
        #Assert
        self.assertEqual("Bishesh", self.a.get_fname())
    def test_gender(self):
        #Assume
        gender = "Bishesh"
        #Action
        result = self.a.set_gender("Male")
        #Assert
        self.assertEqual("Male", self.a.get_gender())
    def test_mobile(self):
        mobile = "roy"
        self.assertRaises(TypeError, self.a.set_mobile, mobile)

    def tearDown(self):
        """
                function to tear down the object
        """
        del self.a




if __name__ == '__main__':
    unittest.main()