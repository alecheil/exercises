from ex_5_13 import falling_distance 
import unittest

class testFallingDistance(unittest.TestCase):
    
    def test_one_second(self):
        expected_value = 4.9
        actual_value = falling_distance(1)
        self.assertEqual(expected_value, actual_value)    
        
    def test_zero_seconds(self):
        expected_value = 0
        actual_value = falling_distance(0)
        self.assertEqual(expected_value, actual_value)

unittest.main()

