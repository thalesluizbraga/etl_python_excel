#In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
#
#def main():
    #...
#
#
#def shorten(word):
    #...
#
#
#if __name__ == "__main__":
    #main()
#Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
#
#pytest test_twttr.py


import pytest
from twttr import shorten

def test_lower():
    assert shorten('maria') == 'mr'
    assert shorten('thales') == 'thls'

def test_capitalize():
    assert shorten('MARIA') == 'MR'
    assert shorten('THALES') == 'THLS'

def test_characters_and_numbers():
    assert shorten("What's up Maria?") == "Wht's p Mr?"
    assert shorten('Hello Thales') == 'Hll Thls'
    assert shorten('thales50') == 'thls50'


# Tem que chamar a funcao do outro doc no teste.
