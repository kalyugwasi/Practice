"""Module providing a function printing python version."""

import sys

def print_python_version():
    print(sys.version)

def response(hey_bob):
    '''
    This function is designed to help return a valid response when 
    something or someone responds to bob, this functions helps
    provide relivent replies as the output
    Parameters
        1. hey_bob (string) :-  Provides the Input for the functions
    Output
        1. return statement (string) based on conditionals
    '''
    stripper = hey_bob.strip()
    if stripper:
        if hey_bob.isupper():
            if stripper[-1] == "?":
                return "Calm down, I know what I'm doing!"
            return "Whoa, chill out!"
        elif stripper[-1] == "?":
            return "Sure."
        return "Whatever."
    return "Fine. Be that way!"
        