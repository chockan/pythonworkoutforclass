What is a Module?

Consider a module to be the same as a code library.

A file containing a set of functions,codes,class you want to include in your application.


Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)


Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")