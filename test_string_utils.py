import pytest
import string_utils

str1 = 'yelena'
str2 = 'JERUSALEM'

def test_string_upper ():
    assert string_utils.make_upper(str1)=='YELENA'

def test_string_lower ():
    assert string_utils.make_lower(str2)=='jerusalem'

#@pytest.mark.utils
def test_check_e ():
    assert string_utils.check_e(str1,'n') == True
    assert string_utils.check_e(str2, 'n') == False
