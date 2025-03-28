#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 01:01:02 2025

@author: mandeepjipty
"""

import pytest
from mod_three import mod_three

def test_mod_three_valid_cases():
    # These test cases correspond to example inputs and expected remainders.
    test_cases = [
        ("1101", 1),   # Binary 1101 (decimal 13) -> 13 % 3 = 1
        ("1110", 2),   # Binary 1110 (decimal 14) -> 14 % 3 = 2
        ("1111", 0),   # Binary 1111 (decimal 15) -> 15 % 3 = 0
        ("1010", 1),   # Binary 1010 (decimal 10) -> 10 % 3 = 1
        ("110",  0)    # Binary 110  (decimal 6)  -> 6 % 3 = 0
    ]
    for binary_str, expected in test_cases:
        result = mod_three(binary_str)
        assert result == expected, f"For input '{binary_str}', expected {expected} but got {result}"

def test_mod_three_invalid_input():
    # The FSM should raise a ValueError when encountering invalid symbols.
    with pytest.raises(ValueError):
        mod_three("1021")  # '2' is not a valid binary digit.

def test_mod_three_empty_input():
    # If an empty string is provided, our FSM remains in the initial state,
    # which corresponds to a remainder of 0.
    assert mod_three("") == 0