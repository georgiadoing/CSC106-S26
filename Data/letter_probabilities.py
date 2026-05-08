###
# letter_probabilities.py
#
# author: Kristina Striegnitz
#
# version: winter 2017
#
###

# If we randomly pick a letter from an English text, how likely is it
# that this letter is an "a", a "b", etc.? Given a letter, this
# function tells you what that probability is.
# Based on https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
def letter_prob( c ):
    """ If c is an alphabetic character, we return its unigram
        probability (for english), otherwise we return 1.0. We ignore
        capitalization.
    """
    d = {'e':0.1202,
         't':0.0910,
         'a':0.0812,
         'o':0.0768,
         'i':0.0731,
         'n':0.0695,
         's':0.0628,
         'r':0.0602,
         'h':0.0592,
         'd':0.0432,
         'l':0.0398,
         'u':0.0288,
         'c':0.0271,
         'm':0.0261,
         'f':0.0230,
         'y':0.0211,
         'w':0.0209,
         'g':0.0203,
         'p':0.0182,
         'b':0.0149,
         'v':0.0111,
         'k':0.0069,
         'x':0.0017,
         'q':0.0011,
         'j':0.0010,
         'z':0.0007
         }
    if c.lower() in d:
        return d[c.lower()]
    else:
        return 1.0


