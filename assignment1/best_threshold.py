#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:50:03 2025

@author: mandeepjipty
"""

"""
Assignment 1:-

We are evaluating a binary classification model. 
We have the number of true positives, true negatives, false positives, 
and false negatives for confidence score thresholds 
0.1, 0.2, 0.3, ..., 0.9 respectively.
Write a function to return THE BEST threshold that yields a recall >= 0.9

"""

def best_threshold(metrics, min_recall=0.9):
    """
    Given a list of metric dictionaries for different thresholds,
    returns the threshold that has at least min_recall and 
    the highest precision among those.

    Parameters:
        metrics (list of dict): Each dict must include keys 
        'threshold', 'tp', 'fp', 'tn', 'fn'.
        min_recall (float): The minimum required recall (default is 0.9).

    Returns:
        float or None: The best threshold, or None if no threshold meets 
        the recall requirement.
    """
    best_choice = None
    best_prec = -1.0 

    for entry in metrics:
        tp = entry.get('tp', 0)
        fp = entry.get('fp', 0)
        fn = entry.get('fn', 0)

        if tp + fn == 0:
            # Skip if there are no positive cases.
            continue

        rec = tp / (tp + fn)
        if rec >= min_recall:
            if tp + fp > 0:
                prec = tp / (tp + fp) # we calculate precision to reduce false positives
            else:
                prec = 0.0

            if prec > best_prec: 
                best_prec = prec
                best_choice = entry['threshold']
    
    return best_choice


if __name__ == '__main__':
    # Simulated data for a test set of 1,000 samples:
    # 200 actual positives and 800 negatives.
    # Lower thresholds yield higher recall but lower precision,
    # while higher thresholds yield higher precision but lower recall.
    metrics = [
        {'threshold': 0.1, 'tp': 195, 'fn': 5,   'fp': 750, 'tn': 50},
        {'threshold': 0.2, 'tp': 190, 'fn': 10,  'fp': 600, 'tn': 200},
        {'threshold': 0.3, 'tp': 185, 'fn': 15,  'fp': 400, 'tn': 400},
        {'threshold': 0.4, 'tp': 175, 'fn': 25,  'fp': 300, 'tn': 500},
        {'threshold': 0.5, 'tp': 160, 'fn': 40,  'fp': 200, 'tn': 600},
        {'threshold': 0.6, 'tp': 140, 'fn': 60,  'fp': 100, 'tn': 700},
        {'threshold': 0.7, 'tp': 120, 'fn': 80,  'fp': 50,  'tn': 750},
        {'threshold': 0.8, 'tp': 100, 'fn': 100, 'fp': 20,  'tn': 780},
        {'threshold': 0.9, 'tp': 80,  'fn': 120, 'fp': 10,  'tn': 790},
    ] 
    # data structure selected for the simulated data is a list of dictionaries 
    # because we need to iterate over the confidence scores to get 
    # the best threshold. 
    # The inner data structure is a dictionary which helps in o(1) lookup 
    # of a specific input value.

    result = best_threshold(metrics, min_recall=0.9)
    if result is not None:
        print("The best threshold with recall >= 0.9 is:", result)
    else:
        print("No threshold meets the required recall.")
