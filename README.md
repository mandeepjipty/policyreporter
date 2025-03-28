# Software Developer Technical Assignments

This repository contains my solutions to two technical assignments for the Software Developer position.

## Assignments Overview

1. **Assignment 1: Best Threshold for Binary Classification Model**
   - **Location:** `assignment1/`
   - **Description:** Implements a function that selects the best confidence threshold for a binary classification model. The function evaluates various thresholds to ensure that recall is at least 0.9 and then selects the threshold with the highest precision.
   - **Further Details:** See the `assignment1/README.md` file for instructions on running the code and more details on the implementation.

2. **Assignment 2: Mod-Three Using a Finite State Machine (FSM)**
   - **Location:** `assignment2/`
   - **Description:** Implements a solution to compute the remainder when an unsigned binary integer is divided by three using a Finite State Machine (FSM). This solution is built in an object-oriented manner and uses the exact symbols from the assignment (Q, Σ (Sigma), q0, δ (delta), and state_to_remainder).
   - **Further Details:** Refer to the `assignment2/README.md` file for a detailed explanation of the design, setup instructions, and how to run both the program and its tests.

## Directory Structure
├── assignment1
│   ├── README.md
│   └── best_threshold.py
└── assignment2
    ├── README.md
    ├── finite_state_machine.py
    ├── mod_three.py
    └── test_mod_three.py

## Installation Requirements

- **Python 3:** Ensure that Python 3 is installed on your system.
- **pytest:** For running the test cases in Assignment 2, install pytest. You can install it via pip:
  ```bash
  pip3 install pytest

## How to Run

- **For Assignment 1:**
  1. Navigate to the `assignment1/` directory.
  2. Follow the instructions in the `README.md` file to run the code.

- **For Assignment 2:**
  1. Navigate to the `assignment2/` directory.
  2. To run the mod-three program, execute:
     ```bash
     python mod_three.py
     ```
  3. To run the tests with pytest, execute:
     ```bash
     pytest test_mod_three.py
     ```
