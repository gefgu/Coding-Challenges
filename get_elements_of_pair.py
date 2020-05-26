"""Cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons. Implement car and cdr."""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def get_first(a, b):
        return a
    return f(get_first)

def cdr(f):
    def get_last(a, b):
        return b
    return f(get_last)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
