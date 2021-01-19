import unittest
import add

# ===========================================
# Run test with "python -m unittest -v" v means verbose
# ===========================================
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("To setup")

    def test_addition(self):
        ''' To give comment for test  - will only work for test not for setUp or teatDown'''
        num = 10
        result = add.sum5(num)
        self.assertEqual(result, 15)

    def test_addition_Error(self):
        num = "sdfsfddsf"
        result = add.sum5(num)
        #self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_input_None(self):
        num = None
        result = add.sum5(num)
        self.assertEqual(result, "Please enter a number")

    def test_input_empty(self):
        ''' To give comment for test '''
        num = ""
        result = add.sum5(num)
        self.assertEqual(result, "Please enter a number")

    def tearDown(self):
        print("To clean up")

    def abc(self):
        print("Any methid")

# with this we can run multiple test files
if __name__ == "__main__":
    unittest.main()
