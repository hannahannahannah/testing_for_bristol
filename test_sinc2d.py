"""This is to test the function fib.py"""
from sinc2d import *

def test_sinc2d_0():
    sinc2d0_expected = 1.0
    sinc2d0_calculated= sinc2d(0,0)
    assert sinc2d0_calculated == sinc2d0_expected
