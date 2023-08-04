#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:49:44 2023

@author: nebiyousamuel
"""

import math

def compute_unknown_variable(PV=None, PMT=None, r=None, n=None):
    if sum(val is not None for val in [PV, PMT, r, n]) != 3:
        raise ValueError("Please provide exactly 3 out of 4 variables.")

    if PV is None:
        PV = PMT * (1 - (1 + r)**(-n)) / r
        return PV

    if PMT is None:
        PMT = PV * (r * (1 + r)**n) / ((1 + r)**n - 1)
        return PMT

    if r is None:
        r = ((PMT / PV) + 1)**(1 / n) - 1
        return r

    if n is None:
        n = math.log((PMT / (PMT - r * PV))) / math.log(1 + r)
        return n

def get_input():
    print("Enter values for three variables (leave the unknown variable empty):")
    PV = input("Present Value (PV): ")
    PMT = input("Payment (PMT): ")
    r = input("Interest Rate (r): ")
    n = input("Number of Periods (n): ")

    if PV:
        PV = float(PV)
    if PMT:
        PMT = float(PMT)
    if r:
        r = float(r)
    if n:
        n = float(n)

    return PV, PMT, r, n

if __name__ == "__main__":
    PV, PMT, r, n = get_input()
    unknown_variable = compute_unknown_variable(PV, PMT, r, n)
    print(f"The unknown variable is: {unknown_variable}")
