Python Modules
Introduction

A module is a Python file with a .py extension that contains reusable code such as functions, classes, variables, and executable statements. Modules allow developers to divide large programs into smaller, organized files, making code easier to understand, maintain, and reuse. Instead of rewriting the same code in multiple programs, developers can create a module once and import it wherever needed.

Modules are one of the core features of Python and play an important role in building scalable and maintainable applications.

Why Use Modules?

Modules provide several advantages:

Promote code reusability by allowing the same code to be used in multiple projects.
Improve readability by separating code into logical files.
Simplify debugging and maintenance.
Reduce code duplication.
Allow collaboration among multiple developers by dividing a project into independent components.
Creating a Module

A module is simply a Python file saved with the .py extension.

Example:

# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

The filename (calculator.py) becomes the module name.

Importing Modules

Python provides several ways to import modules.

Import Entire Module

Imports the complete module. Functions and variables are accessed using the module name.

import calculator

calculator.add(5, 3)
Import Specific Objects

Imports only the required functions or variables.

from calculator import add

add(5,3)
Import Multiple Objects
from calculator import add, subtract
Import Using Alias

A module can be imported with a shorter name using the as keyword.

import calculator as calc

calc.add(10,20)

Functions can also be imported with aliases.

from calculator import add as addition

addition(5,6)
Import All Objects
from calculator import *

Although this imports every public object from the module, it is generally discouraged because it can create namespace conflicts and reduce code readability.

Module Namespace

Each module has its own namespace. Functions, variables, and classes inside a module do not interfere with objects in other modules.

Objects inside a module are accessed using dot notation.

Example:

import math

math.sqrt(25)
math.pi
Executing Modules as Scripts

A module can be executed directly or imported into another program.

Python provides the special variable __name__.

When a file is executed directly,

__name__ == "__main__"

When imported,

__name__

contains the module name.

Example:

def greet():
    print("Hello")

if __name__ == "__main__":
    greet()

This allows the module to contain testing code without executing it when imported.

Module Search Path

When importing a module, Python searches in the following order:

Current working directory
Directories listed in the PYTHONPATH environment variable
Standard Python Library
Installed third-party packages (site-packages)

The search path can be viewed using:

import sys

print(sys.path)
Reloading Modules

If a module is modified after being imported, Python does not automatically reload it.

The module can be reloaded using:

import importlib
import calculator

importlib.reload(calculator)
Built-in Modules

Python provides many built-in modules that offer ready-made functionality.

Some commonly used built-in modules include:

Module	Description
math	Mathematical operations
random	Random number generation
os	Operating system interaction
sys	Interpreter and system information
datetime	Date and time operations
json	JSON data handling
statistics	Statistical calculations
collections	Specialized container data types

Example:

import random

random.randint(1,10)
The dir() Function

The dir() function returns a list of names defined inside a module.

Example:

import math

dir(math)

It is useful for exploring available functions and attributes.

Python Packages

A package is a collection of related Python modules organized in directories.

Packages help organize large applications into multiple modules.

Example structure:

project/

    utilities/

        __init__.py

        math_utils.py

        string_utils.py

The __init__.py file identifies the directory as a Python package.

Importing from Packages

Entire module:

from utilities import math_utils

Specific function:

from utilities.math_utils import add
Absolute Imports

Absolute imports specify the complete path from the project's root.

Example:

from utilities.math_utils import add

Absolute imports improve readability and are commonly used in larger projects.

Relative Imports

Relative imports use dots (.) to refer to modules within the same package.

Example:

from . import math_utils

from ..utilities import string_utils

Relative imports are mainly used inside packages.

all Variable

The __all__ variable controls which modules or objects are imported when using

from package import *

Example:

__all__ = ["math_utils", "string_utils"]
Common Errors
ModuleNotFoundError

Occurs when Python cannot locate the specified module.

Example:

import abcxyz

Output:

ModuleNotFoundError
ImportError

Occurs when trying to import an object that does not exist.

Example:

from math import square

Output:

ImportError
Best Practices
Divide large programs into multiple modules.
Keep one logical purpose per module.
Place import statements at the beginning of the file.
Avoid using from module import *.
Use meaningful module names.
Use aliases only when necessary.
Group related modules into packages.
Use if __name__ == "__main__": for testing executable code.
Summary
A module is a reusable Python file containing functions, classes, variables, and executable statements.
Modules improve code organization, readability, maintenance, and reusability.
Python supports multiple ways to import modules.
Packages organize related modules into directories.
The dir() function lists available names in a module.
Built-in modules provide ready-to-use functionality.
The __name__ == "__main__" construct allows a module to function both as a reusable library and as a standalone script.
Following module best practices leads to cleaner, scalable, and maintainable Python applications.