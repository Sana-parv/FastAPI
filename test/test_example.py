import pytest

def test_equal_or_not():
    assert 2 == 2

def test_is_instance():
    assert isinstance('sana',str)
    assert isinstance(2,int)

def test_boolean():
    validate = True
    assert validate is True
    assert ('hello' == 'world') is False

def test_type():
    assert type('hello' is str)
    assert type('world' is not int)

def test_greater_or_lower():
    assert 5 < 7

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False,True,True,True,False]
    assert 1 in num_list
    assert all( num_list)  #all(): → every value must be True
    assert any(any_list)  #any() : at least one value must be True


class Student:
    def __init__(self,frst_name: str,last_name:str,major: str,years: int):
        self.frst_name = frst_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_employee():
    return Student('john','Doe','Computer science',3)



def test_student(default_employee):
    assert default_employee.frst_name == 'john','frst name should be john'
    assert default_employee.last_name == 'Doe','last_name should be Doe'
    assert default_employee.major == 'Computer science','major should be Computer science'
    assert default_employee.years == 3,'years should be 3'