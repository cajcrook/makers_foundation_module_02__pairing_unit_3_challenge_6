import pytest
from lib.age_checker import age_checker

"""
Check valid age
Return = Access Granted
"""
def test_valid_age():
    assert age_checker('1990-09-13') == "Access Granted"

"""
Check invalid age
Return = "Access denied, current age: 4, you need to be 16"
"""
def test_invalid_age():
    assert age_checker('2020-09-13') == "Access Denied, current age: 3, you need to be 16"

"""
Check format of string is correct "YYYY-MM-DD"
Return if format is invalid - Error Message "Age format is incorrect"
"""
def test_date_format_is_correct():
    with pytest.raises(Exception) as err:
        age_checker('13-09-2022')
    assert str(err.value) == "Age format is incorrect"



