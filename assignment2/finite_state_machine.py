#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 00:34:49 2025

@author: mandeepjipty
"""


class FiniteStateMachine:
    def __init__(self, Q, Sigma, q0, delta):
        """
        Initialize the FSM.
        
        :param Q: List of states (finite set Q).
        :param Sigma: List of valid input symbols (alphabet sigma).
        :param q0: The initial state (q0).
        :param delta: Transition function delta as a dictionary:
                      { current_state: { symbol: next_state } }.
        """
        self.Q = Q
        self.Sigma = Sigma
        self.q0 = q0
        self.delta = delta

    def process(self, input_str):
        """
        Process an input string symbol by symbol using the transition function delta.
        
        :param input_str: A string consisting of symbols from sigma.
        :return: The final state after processing the input.
        :raises ValueError: If an input symbol is not in Σ.
        """
        current_state = self.q0
        for symbol in input_str:
            if symbol not in self.Sigma:
                raise ValueError(f"Invalid symbol '{symbol}'. Allowed symbols: {self.Sigma}")
            current_state = self.delta[current_state][symbol]
        return current_state
