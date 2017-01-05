"""This is to test the function fib.py"""
from fib import *

def test_fib_0():
    fib0_expected = 1
    fib0_calculated= fib(0)
    assert fib0_calculated == fib0_expected

def test_fib_4():
    fib4_expected = 5
    fib4_calculated= fib(4)
    assert fib4_calculated == fib4_expected

def test_fib_5():
    fib5_expected = 8
    fib5_calculated= fib(5)
    assert fib5_calculated == fib5_expected
