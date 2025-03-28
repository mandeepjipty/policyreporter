#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 00:36:40 2025

@author: mandeepjipty
"""



from finite_state_machine import FiniteStateMachine

Q = ['S0', 'S1', 'S2']     # three states
Sigma = ['0', '1']         # The binary input symbols.
q0 = 'S0'                  # Initial state.
F = Q                      # Final states 

# Define the transition function delta based on:
delta = {
    'S0': {'0': 'S0', '1': 'S1'},
    'S1': {'0': 'S2', '1': 'S0'},
    'S2': {'0': 'S1', '1': 'S2'}
}

# Map the final state to the actual remainder.
state_to_remainder = {
    'S0': 0,
    'S1': 1,
    'S2': 2
}

def mod_three(binary_str):
    """
    Compute the remainder when the unsigned binary integer (given as binary_str)
    is divided by three using a Finite State Machine.
    
    :param binary_str: A string of binary digits .
    :return: An integer remainder (0, 1, or 2).
    """
    fsm = FiniteStateMachine(Q, Sigma, q0, delta)
    final_state = fsm.process(binary_str)
    return state_to_remainder[final_state]


   


if __name__ == "__main__":
    
    
    # Example test cases: binary string and remainders
    test_cases = [
        ("1101", 1),   
        ("1110", 2),   
        ("1111", 0),   
        ("1010", 1),   
        ("110",  0)    
    ]
    
    for binary_str, expected in test_cases:
        result = mod_three(binary_str)
        print(f"Input: {binary_str} -> Remainder: {result} (Expected: {expected})")