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
    