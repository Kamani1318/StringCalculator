import pytest
import random
import numpy as np
from iter_1 import string_calc

def test_with_empty_string():
    assert string_calc("") == 0
    
def test_with_one_number():
    assert string_calc("1") == 1

def test_with_two_numbers():
    assert string_calc("1,2") == 3
    
def test_with_unknown_numbers():
    assert string_calc("1,2,3,5") == 11
    
def test_with_new_line():
    assert string_calc("1\n2,3") == 6
    
def test_with_comma_before_newline():
    with pytest.raises(ValueError):
        string_calc("1,\n")
        
def test_with_different_delimiters():
    assert string_calc("//;\n1;2") == 3
    
def test_with_negative_numebrs():
    with pytest.raises(ValueError):
        string_calc("-1,2,3")

    


    

    