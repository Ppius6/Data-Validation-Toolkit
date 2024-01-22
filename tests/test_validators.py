# Implementation of test_validators.py for testing the DataValidator class

import unittest
from datavalidationtoolkit.validators import Validator

class TestDataValidator(unittest.TestCase):
    """
    Test case for the DataValidator class.
    """
    
    # Test email_validator() method
    def test_is_valid_email(self):
        # Positive test cases
        self.assertTrue(Validator.is_valid_email("test@example.com"))
        # Negative test cases
        self.assertFalse(Validator.is_valid_email("test@.com"))
        
    # Test is_valid_phone_number() method
    def test_is_valid_phone_number(self):
        # Positive test cases
        self.assertTrue(Validator.is_valid_phone_number("+254712345678"))
        # Negative test cases
        self.assertFalse(Validator.is_valid_phone_number("254712345678"))
        
    # Test is_valid_url() method
    def test_is_valid_url(self):
        # Positive test cases
        self.assertTrue(Validator.is_valid_url("https://example.com"))
        # Negative test cases
        self.assertFalse(Validator.is_valid_url("example.com"))
        
    # Test is_valid_custom() method
    def test_is_valid_custom(self):
        # Positive test cases
        self.assertTrue(Validator.is_valid_custom("test", r"^\w+$"))
        # Negative test cases
        self.assertFalse(Validator.is_valid_custom("test", r"^\d+$"))
        
# Run tests
unittest.main()