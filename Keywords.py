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
import random

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

# include module
def _import():
    r = random.randint(1, 2)
    return r > 0 and r < 3

# check set contains a value
def _in():
    array = [ 0, 1, 2, 3, 4, 5 ]
    return 3 in array

# check object equality
def _is():
    x = 5
    y = x   # is compares the address of the objects not the contents
    # python memory manager may reuse objects such as small integers through caching
    # as a result two variables which are not linked may reference the same address
    return x is y

# make anonymous functions
def _lambda():
    add = lambda a, b : a + b   # lambda is best used for local functions that are small/simple
    x = add(add(1,2), 5)
    return x == 8

# special type for null/void values
def _none():
    x = None    # none is like null except it is treated as a unique type (NoneType)
    y = 5
    return x == None and x is not y

# exposes a nested variable to outer function
def _nonlocal():
    x = 0
    def local():
        nonlocal x  # restricted form of global
        x = 5
    local()
    return x == 5

# logical NOT operator
def _not():
    return not 1 == 0

# logical OR operator
def _or():
    true1 = True or True
    true2 = True or False
    true3 = False or True
    false = False or False
    return true1 and true2 and true3 and not false

# make stub methods
def _pass():
    def local():
        pass    # can also be used in classes and ifs
    local()
    return True

# throw an exception
def _raise():
    try:
        raise Exception
    except:
        return True

# push value(s) to stack for caller to use
def _return():
    return 0 == 0   # evaluates expression before jump     

# operator for built-in boolean
def _true():
    return True

# start an exception handler block
def _try():
    try:
        x = 10
    finally:
        return True

# make a loop
def _while():
    i = 0
    while i < 10:
        i += 1
    return i == 10

# simplify exception handler
def _with():
    with open("README.md", "r") as file:    # similar to 1 line using statements
        o = file.readline()   # in practice it shortens exception handlers (eg. file.open)
    return o[0] == '#'

# lazy iterator (evaluates expressions only when used)
def _yield():
    def local():
        for i in range(100):
            yield i
    iterator = local()
    while next(iterator) != 50: # next requests iterator to continue execution
        continue
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

inline("import...")
AssertPass(_import())

inline("in...")
AssertPass(_in())

inline("is...")
AssertPass(_is())

inline("lambda...")
AssertPass(_lambda())

inline("none...")
AssertPass(_none())

inline("nonlocal...")
AssertPass(_nonlocal())

inline("not...")
AssertPass(_not())

inline("or...")
AssertPass(_or())

inline("pass...")
AssertPass(_pass())

inline("raise...")
AssertPass(_raise())

inline("return...")
AssertPass(_return())

inline("true...")
AssertPass(_true())

inline("try...")
AssertPass(_try())

inline("while...")
AssertPass(_while())

inline("with...")
AssertPass(_with())

inline("yield...")
AssertPass(_yield())