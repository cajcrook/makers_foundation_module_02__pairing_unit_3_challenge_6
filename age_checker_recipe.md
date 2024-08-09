# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def age_checker():
parameters: string in format "YYY-MM-DD"
return:
    'Access granted' if over 16yrs.
    ('Access denied' + "user age" + "you need to be 16") if < 16yrs

side effect:
Check format of input is valid.

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Check valid age
Return = Access Granted
"""
age_checker('1990-09-13')
return 'Access granted'

"""
Check invalid age
Return = "Access denied, current age: 4, you need to be 16"
"""
age_checker('2020-09-13')
return "Access denied, current age: 4, you need to be 16"

"""
Check format of string is correct "YYYY-MM-DD"
Return if format is invalid - Error Message "Age format is incorrect"

""


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
