# Data Validation Toolkit

## Overview
Data Validation Toolkit is a Python package that provides easy-to-use functions for validating various types of data. It is designed to be a handy tool for applications needing to validate email addresses, phone numbers, URLs, and custom regular expressions.

## Installation
To install Data Validation Toolkit, run the following command:

```
pip install datavalidationtoolkit
```

## Usage
Here are some examples of how to use the Data Validation Toolkit:

```
from datavalidationtoolkit.validators import DataValidator

# Validate an email address
valid_email = DataValidator.is_valid_email("user@example.com")
print(f"Email valid: {valid_email}")

# Validate a phone number
valid_phone = DataValidator.is_valid_phone_number("+1234567890")
print(f"Phone number valid: {valid_phone}")

# Validate a URL
valid_url = DataValidator.is_valid_url("https://www.example.com")
print(f"URL valid: {valid_url}")

# Validate with a custom regex
valid_custom = DataValidator.is_valid_custom("123ABC", r"^\d{3}[A-Z]{3}$")
print(f"Custom validation: {valid_custom}")
```

## Contributing
Contributions to the Data Validation Toolkit are welcome! If you have suggestions for improvement or have found a bug, please open an issue or submit a pull request.

