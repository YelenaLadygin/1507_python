import pytest
import school

grades = [1,3,7,99]

def test_school_aver ():
    assert school.calculate_average(grades)==27.5

def test_add_bonus ():
    assert school.add_bonus(grades)==[6, 8, 12, 104]

@pytest.mark.result
def test_get_result ():
    assert school.get_result(100)=='excellent'
    assert school.get_result(56)=='fall'

