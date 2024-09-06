#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    soma1 = Signal(bool(0))
    carry1 = Signal(bool(0))
    carry2 = Signal(bool(0))

    ha1 = halfAdder(a, b, soma1, carry1)
    ha2 = halfAdder(soma1, c, soma, carry2)

    @always_comb
    def logic():
        carry.next = carry1 | carry2  

    return ha1, ha2, logic

@block
def adder2bits(x, y, soma, vaiUm):
    c = Signal(bool(0))
    half = halfAdder(x[0],y[0],soma[0],c)

    full = fullAdder(x[1],y[1],c,soma[1],vaiUm)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)

    vaium = [Signal(bool(0)) for i in range(n)]
    faList = [None for i in range(n)]

    for i in range(n):
        faList[i] = fullAdder(x[i], y[i], vaium[i - 1], soma[i], vaium[i])

    return instances()