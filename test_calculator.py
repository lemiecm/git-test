import calculator as calc
import unittest
#An empty string returns zero

class TestStringMethods(unittest.TestCase): 
    # test function to test equality of two value 
    def test_empty_input(self):
    
        #Given
        input_number = ""
        expected_result = 0
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)

    def test_single_value(self):
    
        #Given
        input_number = "12"
        expected_result = 12
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)
    def test_coma_sum(self):
    
        #Given
        input_number = "11,23"
        expected_result = 34
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)
    def test_newline_sum(self):
    
        #Given
        input_number = "11\n23"
        expected_result = 34
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)
    def test_general_sum(self):
    
        #Given
        input_number = "11\n11,11"
        expected_result = 33
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)
        
    def test_negative_num(self):
    
        #Given
        input_number = "-11"
        
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertRaises(result)
        

    def test_very_big_num(self):
    
        #Given
        input_number = "1001"
        expected_result = 0
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)

    def test_extra_separator(self):
    
        #Given
        input_number = "//#13#4"
        expected_result = 17
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)




if __name__ == "__main__":
    unittest.main()


   
