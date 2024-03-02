import pytest
#Imagine we have a function that adds 2 numbers and returns the result

#1. Write a basic test that ensures the function returns the correct result

def test_add():
    assert add(2, 3) == 5


def add(a, b):
    return a + b    

def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3) 


#add("two", 3)  This will raise a TypeError

def test_multiply():
    assert multiply(2, 3) == 6


def multiply(a, b):
    return a * b

def test_subtract():
    assert subtract(5, 3) == 2

def subtract(a, b):
    return a - b

def test_divide():
    assert divide(6, 3) == 2

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


def test_compare():
    assert compare(5, 5) == True
    assert compare(5, 6) == False

def compare(a, b):
    return a == b   
