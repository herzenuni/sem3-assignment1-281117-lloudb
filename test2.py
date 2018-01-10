import pytest
import task2

def test_1():
    assert task2.func1() == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92]

def test_2():
    assert task2.func2(2) == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92]

def factory(a, b):
    def abstrct_test():
        assert task2.func2(a) == b
    return abstrct_test

test_3 = factory(2, [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])
