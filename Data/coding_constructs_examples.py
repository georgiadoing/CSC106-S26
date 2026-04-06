########################################
# Georgia Doing
# 4/6/26
# coding_constructs.py
#
# In-class examples of coding constructs to help
# keep your code DRY (Don't Repeat Yourself)
########################################

# Comments
# example syntax for a 1-line comment
''' example syntax for
a multi-line comment'''
""" another example syntax
for a multi-line comment"""
# semantics: the interpreter ignores all
#   code written aftern # or between tripple
#   quotes (single or double)

# Variables
# syntax: <var_name> = <value>
# semantics: save value to names memory block
# example: save int 5 to name x
x = 5
print("Variable named 'x' has the value:", x)

# For Loops
# syntax: for <var> in range(<reps>):
#           <lines>
# semantics: repeat lines reps number of times
# example: print "Hi" 3 times
for h in range(3):
    print('Hi')

# Calling functions
# syntax: <function_name>()
# semantics: run the lines of code saved to
#   the name <function_name>
# example: call print function
print('The print function is being called')

# Loading Modules/Libraries
# syntax: import <lib_name>
# semantics: load functions, variables from lib
#   into program running memory
# example: load turtle library
import turtle

# Using Library Functions
# syntax: <lib_name>.<function_name>()
# semantics: call function from library
# example: use turtle forward function
turtle.forward(100)




