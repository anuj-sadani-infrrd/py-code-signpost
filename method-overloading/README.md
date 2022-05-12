# Function overloading in python

## General Definition

`Method overloading` is a form of polymorphism in OOP. Polymorphism allows objects or methods to act in different ways, according to the means in which they are used. One such manner in which the methods behave according to their *argument types and number of arguments* is method overloading

## Python and Overloading
First, one needs to understand the concept of overloading and why it's not applicable to Python.

When working with languages that can **differentiate data types at compile-time**, selecting among the alternatives can occur at compile-time. The act of creating such alternative functions for compile-time selection is usually referred to as overloading a function.

**Python is a dynamically typed language**, so the concept of overloading simply does not apply to it. However, all is not lost, since we can create such alternative functions at run-time:

In programming languages that defer data type identification until run-time the selection among alternative functions must occur at run-time, based on the dynamically determined types of function arguments. Functions whose alternative implementations are selected in this manner are referred to most generally as multimethods.

So we should be able to do multimethods in Python—or, as it is alternatively called: multiple dispatch.
