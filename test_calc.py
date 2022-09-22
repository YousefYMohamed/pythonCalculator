import unittest
import calc

# This class is to test the calc.py class

class TestCalc(unittest.TestCase):

    # defining a function that runs before every test
    def setUp(self):
        pass
    # defining a function that runs after every test
    def tearDown(self):
        pass


    # Defining 4 functions to test each of the 4 operations in the clac module with strings for input values
    def test_add_strings(self):
        result = calc.add("1","2")
        self.assertEqual(result,3)
        
    def test_sub_strings(self):
        result = calc.sub("2","1")
        self.assertEqual(result,1)
    
    def test_mul_strings(self):
        result = calc.mul("2","1")
        self.assertEqual(result,2)
        
    def test_div_strings(self):
        result = calc.div("2","1")
        self.assertEqual(result,2)
        
    
    # Defining 4 functions to test each of the 4 operations in the clac module with integers for input values
    def test_add_ints(self):
        result = calc.add(1,2)
        self.assertEqual(result,3)
        
    def test_sub_ints(self):
        result = calc.sub(2,1)
        self.assertEqual(result,1)
    
    def test_mul_ints(self):
        result = calc.mul(2,1)
        self.assertEqual(result,2)
        
    def test_div_ints(self):
        result = calc.div(2,1)
        self.assertEqual(result,2)
        
    
    # Defining 4 functions to test each of the 4 operations in the clac module with floats for input values
    def test_add_floats(self):
        result = calc.add(1.1,2.1)
        self.assertEqual(result,3.2)
        
    def test_sub_floats(self):
        result = calc.sub(2.1,1.0)
        self.assertEqual(result,1.1)
    
    def test_mul_floats(self):
        result = calc.mul(2.1,1)
        self.assertEqual(result,2.1)
        
    def test_div_floats(self):
        result = calc.div(2.0,1.0)
        self.assertEqual(result,2.0)
    
    # Defining 4 functions to test each of the 4 operations in the clac module with different types for input values
    def test_add_mixedTypes(self):
        result = calc.add(2.1,"3")
        self.assertEqual(result,5.1)
        
    def test_sub_mixedTypes(self):
        result = float("{:.1f}".format(calc.sub(2.1,"3")))
        self.assertEqual(result,-0.9)
        
    def test_mul_mixedTypes(self):
        result = calc.mul(2.0,"-3")
        self.assertEqual(result,-6)
    
    def test_div_mixedTypes(self):
        result = calc.div(2.1,"-2.0")
        self.assertEqual(result,-1.05)    
        

# running the tests on python run
if __name__ == '__main__':
    unittest.main()