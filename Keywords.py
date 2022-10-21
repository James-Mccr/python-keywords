# Code for keywords in python with examples

# Keywords:
# and	A logical operator
# as	To create an alias
# assert	For debugging
# break	To break out of a loop
# class	To define a class
# continue	To continue to the next iteration of a loop
# def	To define a function
# del	To delete an object
# elif	Used in conditional statements, same as else if
# else	Used in conditional statements
# except	Used with exceptions, what to do when an exception occurs
# False	Boolean value, result of comparison operations
# finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	To create a for loop
# from	To import specific parts of a module
# global	To declare a global variable
# if	To make a conditional statement
# import	To import a module
# in	To check if a value is present in a list, tuple, etc.
# is	To test if two variables are equal
# lambda	To create an anonymous function
# None	Represents a null value
# nonlocal	To declare a non-local variable
# not	A logical operator
# or	A logical operator
# pass	A null statement, a statement that will do nothing
# raise	To raise an exception
# return	To exit a function and return a value
# True	Boolean value, result of comparison operations
# try	To make a try...except statement
# while	To create a while loop
# with	Used to simplify exception handling
# yield	To end a function, returns a generator

import math as alias
from datetime import time

def inline(msg):
    print(msg, end = "")

def AssertPass(passed):
    if passed:
        ok()
    else:
        fail()

def ok():
    print("OK")

def fail():
    print("ERROR")
    quit()

# logical AND operator
def _and():
    # Truth table
    true = True and True
    false1 = False and True
    false2 = True and False
    false3 = False and False
    return true and not false1 and not false2 and not false3

# create an alias (see imports)
def _as():
    o = alias.pow(2, 5)
    return o == 32

# assert an expression is True
def _assert():
    assert (5 > 4) == True
    return True

# jump to next instruction outside most recent loop
def _break():
    x = False
    while True:
        x = True
        break
    return x

# define a custom data structure
def _class():
    class Door:
        def __init__(self):
            self.isOpen = False
        
        def open(self):
            self.isOpen = True

        def close(self):
            self.isOpen = False

    d = Door()
    d.open()
    if not d.isOpen:
        return False
    d.close()
    if d.isOpen:
        return False
    return True

# jump to start of most recent loop
def _continue():
    c = 0
    while c < 10:
        c+=1
        continue
        print("X")  # continue jumps, thus never reaches this
    return True

# define function
def _def():
    def OneTwo():
        return (1 + 2) == 3
    return OneTwo()

# delete an object (free allocated memory)
def _del():
    x = "an example of del"
    del x   # x becomes undefined
    return True

# create an extra conditioned branch in an if statement
def _elif():
    if 1 == 0:
       return False
    elif 1 == 1:
        return True

# unconditional if branch
def _else():
    if 1 == 0:
        return False
    else:
        return True

# catch an unhandled exception
def _except():
    try:
        raise Exception
    except:
        return True

# operator for in-built boolean type
def _false():
    return not False

# block of code to always execute in try statement
def _finally():
    try:
        x = 5 + 3
    finally:
        del x
        return True # in practice it is used to clean up resources

# iterate sequences
def _for():
    j = 0
    for i in range(1, 10):
        j += i
    return j == 45

# include a specific section from module
def _from():
    x = time(hour=1)
    return x.hour == 1

# scope to whole program
def _global():
    def local():
        global gx
        gx = 12
    local()
    return gx == 12

# branch execution of instructions
def _if():
    if True:
        return True


inline("and...")
AssertPass(_and())

inline("as...")
AssertPass(_as())

inline("assert...")
AssertPass(_assert())

inline("break...")
AssertPass(_break())

inline("class...")
AssertPass(_class())

inline("continue...")
AssertPass(_continue())

inline("def...")
AssertPass(_def())

inline("del...")
AssertPass(_del())

inline("elif...")
AssertPass(_elif())

inline("else...")
AssertPass(_else())

inline("except...")
AssertPass(_except())

inline("false...")
AssertPass(_false())

inline("finally...")
AssertPass(_finally())

inline("for...")
AssertPass(_for())

inline("from...")
AssertPass(_from())

inline("global...")
AssertPass(_global())

inline("if...")
AssertPass(_if())