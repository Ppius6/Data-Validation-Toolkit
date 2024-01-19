# Implementation of the validators.py module for the Data Validation Toolkit package

# Importing necessary libraries
import re
from urllib.parse import urlparse

# Validator class

class Validator:
    """
    A class that provides static methods for validating data.
    """
    
    @staticmethod
    # Email Validation Function
    def email_validator(email):
        """
        Validate an email address using regex.
        
        Args:
            email (str): Email address to be validated.
            
        Returns:
            bool: True if email is valid, False otherwise.
        """
        
        # Regular expression for email validation
        regex = r'^\w+[\w\.-]*@\w+[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None
    
    @staticmethod
    # Phone Number Validation Function
    def is_valid_phone_number(phone):
        """
        Validate a phone number using regex.
        
        Args:
            phone (str): Phone number to be validated.
            
        Returns:
            bool: True if phone number is valid, False otherwise.
        """
        
        # Regular expression for phone number validation
        regex = r'^\+?[\d\s]{7,15}$'
        return re.match(regex, phone) is not None
    
    @staticmethod
    # URL Validation Function
    def is_valid_url(url):
        """
        Validate a URL.
        
        Args:
            url (str): URL to be validated.
            
        Returns:
            bool: True if URL is valid, False otherwise.
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False
        
    @staticmethod
    # Custom Regex Validation Function
    def is_valid_custom(input_string, pattern):
        """
        Validate a string using a custom regex pattern.
        
        Args:
            input_string (str): String to be validated.
            pattern (str): Regex pattern to be used for validation.
            
        Returns:
            bool: True if string is valid, False otherwise.
        """
        
        # Regular expression for custom validation
        return re.match(pattern, input_string) is not None