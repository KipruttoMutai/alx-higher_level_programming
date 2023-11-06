#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)[:max(0, 2 - len(tuple_a))]
    tuple_b = tuple_b + (0, 0)[:max(0, 2 - len(tuple_b))]
    tuple_c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return tuple_c
