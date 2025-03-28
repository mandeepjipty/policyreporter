# Assignment 2: Mod-Three Using a Finite State Machine (FSM)

## Overview

This project implements a solution to compute the remainder when an unsigned binary integer is divided by three using a Finite State Machine (FSM). Instead of converting the entire binary string to an integer and using the modulus operator, the FSM processes the binary string one symbol at a time.

The FSM is defined using the following notation:
- **Q**: The finite set of states (here, Q = ['S0', 'S1', 'S2']).
- **Σ (Sigma)**: The input alphabet (here, Sigma = ['0', '1']).
- **q0**: The initial state (here, q0 = 'S0').
- **δ (delta)**: The transition function, which is defined as:
  - δ(S0, '0') = S0;  δ(S0, '1') = S1  
  - δ(S1, '0') = S2;  δ(S1, '1') = S0  
  - δ(S2, '0') = S1;  δ(S2, '1') = S2
- **state_to_remainder**: A mapping from the final state to the corresponding remainder:
  - S0 → 0, S1 → 1, S2 → 2

## File Descriptions

### finite_state_machine.py
This file implements a generic Finite State Machine (FSM) class named `FiniteStateMachine`. It uses the symbols as follows:
- **Q**: A list of states.
- **Σ (Sigma)**: The input alphabet.
- **q0**: The initial state.
- **δ (delta)**: The transition function provided as a lookup table, mapping each (current state, input symbol) pair to the next state.

The `process()` method reads an input string one symbol at a time and transitions between states according to δ, finally returning the final state.

### mod_three.py
This file sets up the FSM for the mod-three problem. It defines the following global variables:
- **Q**: `['S0', 'S1', 'S2']` (states representing possible remainders).
- **Σ (Sigma)**: `['0', '1']` (the binary input symbols).
- **q0**: `'S0'` (the initial state).
- **δ (delta)**: The transition function, defined as:
  ```python
  delta = {
      'S0': {'0': 'S0', '1': 'S1'},
      'S1': {'0': 'S2', '1': 'S0'},
      'S2': {'0': 'S1', '1': 'S2'}
  }
  
- **state_to_remainder**: A mapping from final states to remainders:
  ```python
  state_to_remainder = {
      'S0': 0,
      'S1': 1,
      'S2': 2
  }
  
The function `mod_three(binary_str)` creates an instance of `FiniteStateMachine` using these global variables, processes the input string, and returns the corresponding remainder based on the final state.

### test_mod_three.py
This file contains pytest test cases for the mod-three solution:
- **test_mod_three_valid_cases()**: Verifies that a set of valid binary strings returns the correct remainder.
- **test_mod_three_invalid_input()**: Checks that invalid input (non-binary characters) raises a `ValueError`.
- **test_mod_three_empty_input()**: Ensures that an empty string returns the remainder corresponding to the initial state (0).

## How to Run

### To Execute the Mod-Three Program
1. Open a terminal and navigate to the `assignment2` folder.
2. Run:
   ```bash
   python3 mod_three.py
   
The script will print example binary inputs along with their computed remainders and the expected results.

### To Run the Test Cases
1. Ensure that pytest is installed (if not, install it using `pip install pytest`).
2. From the `assignment2` folder, run:
   ```bash
   pytest test_mod_three.py

