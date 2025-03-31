import unittest
from WordToNumber import word_to_num  # Assuming your module is named word_to_num.py

class TestWordToNum(unittest.TestCase):
    """Test cases for word_to_num function."""
    
    def test_simple_numbers(self):
        """Test simple number words."""
        self.assertEqual(word_to_num("one"), 1)
        self.assertEqual(word_to_num("twenty"), 20)
        self.assertEqual(word_to_num("ninety nine"), 99)
        self.assertEqual(word_to_num("one hundred"), 100)
        self.assertEqual(word_to_num("one hundred twenty three"), 123)
    
    def test_american_system(self):
        """Test American number system words."""
        self.assertEqual(word_to_num("one thousand"), 1000)
        self.assertEqual(word_to_num("one thousand two hundred thirty four"), 1234)
        self.assertEqual(word_to_num("ten thousand"), 10000)
        self.assertEqual(word_to_num("fifty thousand six hundred seventy eight"), 50678)
        self.assertEqual(word_to_num("one million"), 1000000)
        self.assertEqual(word_to_num("two million three hundred forty five thousand six hundred seventy eight"), 2345678)
        self.assertEqual(word_to_num("one billion"), 1000000000)
        self.assertEqual(word_to_num("one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"), 1234567890)
    
    def test_indian_system(self):
        """Test Indian number system words."""
        self.assertEqual(word_to_num("one lakh"), 100000)
        self.assertEqual(word_to_num("one lac"), 100000)
        self.assertEqual(word_to_num("one lakhs"), 100000)
        self.assertEqual(word_to_num("two lakh fifty thousand"), 250000)
        self.assertEqual(word_to_num("one crore"), 10000000)
        self.assertEqual(word_to_num("two crore fifty lakh"), 25000000)
        self.assertEqual(word_to_num("five crore sixty seven lakh eighty nine thousand"), 56789000)
    
    def test_extended_system(self):
        """Test extended number system with arba."""
        self.assertEqual(word_to_num("one arba"), 1000000000)
        self.assertEqual(word_to_num("two arba fifty crore"), 2500000000)
        self.assertEqual(word_to_num("five arba sixty seven crore eighty nine lakh"), 5678900000)
        self.assertEqual(word_to_num("one arba two crore three lakh four thousand five hundred six"), 1020304506)
    
    def test_decimal_numbers(self):
        """Test decimal numbers."""
        self.assertEqual(word_to_num("one point five"), 1.5)
        self.assertEqual(word_to_num("twenty point zero two"), 20.02)
        self.assertEqual(word_to_num("one hundred point three two one"), 100.321)
        self.assertEqual(word_to_num("one thousand point five six seven"), 1000.567)
        # Test with Indian system
        self.assertEqual(word_to_num("one lakh point five"), 100000.5)
        self.assertEqual(word_to_num("one crore point two five"), 10000000.25)
        # Test with extended system
        self.assertEqual(word_to_num("one arba point one"), 1000000000.1)
    
    def test_direct_number_input(self):
        """Test direct number string input."""
        self.assertEqual(word_to_num("123"), 123)
        self.assertEqual(word_to_num("1000000"), 1000000)
    
    def test_mixed_formats(self):
        """Test handling of hyphens and extra spaces."""
        self.assertEqual(word_to_num("twenty-two"), 22)
        self.assertEqual(word_to_num("one hundred  and  twenty"), 120)
        self.assertEqual(word_to_num("  fifty   thousand  "), 50000)
    
    def test_error_conditions(self):
        """Test error conditions."""
        with self.assertRaises(ValueError):
            word_to_num(123)  # Non-string input
        
        with self.assertRaises(ValueError):
            word_to_num("")  # Empty string
            
        with self.assertRaises(ValueError):
            word_to_num("hello world")  # No valid number words
            
        with self.assertRaises(ValueError):
            word_to_num("million billion")  # Incorrect order
            
        with self.assertRaises(ValueError):
            word_to_num("thousand million")  # Incorrect order
            
        with self.assertRaises(ValueError):
            word_to_num("lakh crore")  # Incorrect order
            
        with self.assertRaises(ValueError):
            word_to_num("one million one million")  # Repeated term
            
        with self.assertRaises(ValueError):
            word_to_num("one billion thousand")  # Missing million between billion and thousand
            
        with self.assertRaises(ValueError):
            word_to_num("one crore thousand")  # Missing lakh between crore and thousand
            
        with self.assertRaises(ValueError):
            word_to_num("one arba thousand")  # Missing crore and lakh between arba and thousand
            
        with self.assertRaises(ValueError):
            word_to_num("one million one lakh")  # Mixing American and Indian systems
            
        with self.assertRaises(ValueError):
            word_to_num("one arba one billion")  # Mixing extended and American systems
    
    def test_boundary_conditions(self):
        """Test boundary conditions and edge cases."""
        self.assertEqual(word_to_num("zero"), 0)
        self.assertEqual(word_to_num("one hundred and zero"), 100)  # Extra 'and' word
        self.assertEqual(word_to_num("point five"), 0.5)  # Decimal without leading whole number
        
    def test_complex_combinations(self):
        """Test complex combinations of number words."""
        self.assertEqual(word_to_num("nineteen crore eighty four lakh seventy three thousand six hundred and fifty two"), 198473652)
        self.assertEqual(word_to_num("two arba nineteen crore eighty four lakh seventy three thousand six hundred and fifty two"), 2198473652)
        self.assertEqual(word_to_num("nine billion eight hundred seventy six million five hundred forty three thousand two hundred and ten"), 9876543210)

if __name__ == "__main__":
    unittest.main()