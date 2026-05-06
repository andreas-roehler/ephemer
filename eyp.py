#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Blah blub: just a playground. """

import os
import pdb
import random
import re
import sys
import time

# import wx

# app = wx.PySimpleApp()
# frame = wx.Frame(None,-1,"Roulade")
# frame.Show(1)
# app.MainLoop()

# treffer, gruen, rot, schwarz, pair, impair, passe, manque
args = sys.argv
# pdb.set_trace()
# Get the name of the file to count the words in

def usage():
    """Print Fehler. """
    print("""Fehler: %s
Es muß die aufzurufende Ziehungszahl als Argument angegeben werden:
'python roulette.py 1, 'python roulette.py 2', ... 'python roulette.py n'.
""" % (
          os.path.basename(sys.argv[0])))

def main():
    """Some main. """
    if len(sys.argv) == 1:
        usage()
        # sys.exit()

    class Asdf():
        """Asdf. """
        zeit = time.strftime('%Y%m%d--%H-%M-%S')

        # def Utf8_exists(filename) -> a[1:2]:
        # def utf8_exists(self, filename):
        #     """Asdf. """
        #     return os.path.exists(filename.encode('utf-8'))

    def Utf8_exists(self, filename: str) -> bool:
        """Check if file exists and can be read as UTF-8."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                f.read()
            return os.path.exists(filename)
        except (FileNotFoundError, UnicodeDecodeError):
            return False

if __name__ == "__main__":
    main()

import pdb
pdb.set_trace()
try:
    anzahl = int(args[1])
except:
    print("Setze anzahl auf 1")
    anzahl = 1

# class kugel(object) -> a[1:2]:
class kugel(object):
    """Class kugel. """
    zeit = time.strftime('%Y%m%d--%H-%M-%S')
    # zeit = time.strftime('%Y-%m-%d--%H-%M-%S')
    spiel = []
    gruen = [0]
    rot = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    schwarz = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    ausgabe = []
    treffer = None
    fertig = ''
    treffer = random.randint(0, 36)

    def pylauf(self):
        """Eine Doku fuer pylauf"""
        ausgabe = [" "," "," "," "," "," "," "," ", " "]

        ausgabe[0] = treffer
        fertig = ''
#        print("treffer, schwarz, gruen, rot, pair, impair, passe, manque, spiel")
        if treffer in gruen:

            ausgabe[1] = treffer
            ausgabe[2] = treffer
            ausgabe[3] = treffer
            ausgabe[4] = treffer
            ausgabe[5] = treffer
            ausgabe[6] = treffer
            ausgabe[7] = treffer

        elif treffer in schwarz:

            ausgabe[1] = treffer

        elif treffer in rot:

            ausgabe[3] = treffer

        self.geradheit = treffer % 2

        if 0 < self.geradheit:

            ausgabe[5] = treffer
        else:
            if 0 < treffer:

                ausgabe[4] = treffer

        if 0 < treffer:
            if 18 < treffer:

                ausgabe[6] = treffer
            else:

                ausgabe[7] = treffer
        ausgabe[8] = str(i+1)
#        print("ausgabe: %s " % ausgabe)
#        print("len(ausgabe): %s " % len(ausgabe))
        for laenge in range(len(ausgabe)):
            fertig = fertig + ";" + str((ausgabe[laenge]))
        fertig = fertig[1:]
#        print("fertig: %s " % fertig)
        spiel.append(fertig)
        print("treffer: %s " % treffer)
        return treffer
#        print("len(spiel): %s " % len(spiel))

zeit = kugel.zeit
ausgabe = kugel.ausgabe
spiel = kugel.spiel
gruen = kugel.gruen
rot = kugel.rot
schwarz = kugel.schwarz
treffer = kugel.treffer
fertig = kugel.fertig

klauf = kugel()

# with file("roulette-" + zeit + ".csv", 'w') as datei:
#     for i in range(anzahl):
#         klauf.pylauf()
#         datei.write(str(spiel[i]) + " ")

#     datei.write("treffer; schwarz; gruen; rot; pair; impair; passe; manque; spiel")
#     pri

''' asdf' asdf asdf asdf asdf asdfasdf asdfasdf a asdf asdf asdf asdfasdfa asdf asdf asdf asdf
'''

asd = 'asdf asdf asdf asdf asdf asdfasdf asdfasdf a asdf asdf asdf asdfasdfa asdf asdf asdf asdf'

afd = "asdf asdf asdf asdf asdf asdfasdf asdfasdf a asdf asdf asdf asdfasdfa asdf asdf asdf asdf"

a, b, c = (1, 2, 3)
a = b = c = 5
[a, b, c] = 1, 2, 3
a, *b, c = range(10)
inst.a, inst.b, inst.c = 'foo', 'bar', 'baz'
(a, b, *c, d) = x, *y = 5, 6, 7, 8, 9

print('%(language)s has %(number)03d quote types.' %
       {'language': "Python", "number": 2})

print("%(language)s has %(number)03d quote types." %
       {'language': "Python", "number": 4})

(long, sequence, of_items,
    that, needs, to_be, wrapped) = input_list

# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False

# Useful built-in types

# For most types, just use the name of the type in the annotation
# Note that mypy can usually infer the type of a variable from its value,
# so technically these annotations are redundant
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections on Python 3.9+, the type of the collection item is in
# brackets

x: list[int] = [1]
x: set[int] = {6, 7}

# For mappings, we need the types of both keys and values
x: dict[str, float] = {"field": 2.0}  # Python 3.9+

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+

# On Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
from typing import List, Set, Dict, Tuple
x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {"field": 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
x: Tuple[int, ...] = (1, 2, 3)

from typing import Union, Optional

# On Python 3.10+, use the | operator when something could be one of a few types
x: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
# On earlier versions, use Union
x: list[Union[int, str]] = [3, 5, "test", "fun"]

# Use X | None for a value that could be None on Python 3.10+
# Use Optional[X] on 3.9 and earlier; Optional[X] is the same as 'X | None'
x: str | None = "something" if some_condition() else None
if x is not None:
    # Mypy understands x won't be None here because of the if-statement
    print(x.upper())
# If you know a value can never be None due to some logic that mypy doesn't
# understand, use an assert
assert x is not None
print(x.upper())

# Functions

from collections.abc import Iterator, Callable
from typing import Union, Optional

# This is how you annotate a function definition
def stringify(num: int) -> str:
    """Sgring"""
    return str(num)

# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    """Ring. """
    return num1 + num2

# If a function does not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)

# Note that arguments without a type are dynamically typed (treated as Any)
# and that functions without any annotations are not checked
def untyped(x):
    x.anything() + 1 + "string"  # no errors

# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f
def register(callback: Callable[[str], int]) -> None: ...

# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def gen(n: int) -> Iterator[int]:
    """Gen. """
    i = 0
    while i < n:
        yield i
        i += 1

# You can of course split a function annotation over multiple lines
def send_email(
    address: str | list[str],
    sender: str,
    cc: list[str] | None,
    bcc: list[str] | None,
    subject: str = '',
    body: list[str] | None = None,
) -> bool:
    ...

# Mypy understands positional-only and keyword-only arguments
# Positional-only arguments can also be marked by using a name starting with
# two underscores
def quux(x: int, /, *, y: int) -> None:
    pass

quux(3, y=5)  # Ok
quux(3, 5)  # error: Too many positional arguments for "quux"
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

# This says each positional arg and each keyword arg is a "str"
def call(self, *args: str, **kwargs: str) -> str:
    reveal_type(args)  # Revealed type is "tuple[str, ...]"
    reveal_type(kwargs)  # Revealed type is "dict[str, str]"
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)

# Classes

from typing import ClassVar

class BankAccount:
    """The "__init__" method doesn't return anything, so it gets return
     type "None" just like any other method that doesn't return anything_"""
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
        self.account_name = account_name
        self.balance = initial_balance

    # For instance methods, omit type for "self"
    def deposit(self, amount: int) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

        self.balance -= amount

# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 400)
def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
    src.withdraw(amount)
    dst.deposit(amount)

# Functions that accept BankAccount also accept any subclass of BankAccount!
class AuditedBankAccount(BankAccount):
    # You can optionally declare instance variables in the class body
    audit_log: list[str]

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AuditedBankAccount("Bob", 300)
transfer(audited, account, 100)  # type checks!

# You can use the ClassVar annotation to declare a class variable
class Car:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]

# If you want dynamic attributes on your class, have it
# override "__setattr__" or "__getattr__"
class A:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...

a = A()
a.foo = 42  # Works
a.bar = 'Ex-parrot'  # Fails type checking

# When you’re puzzled or when things are complicated

from typing import Union, Any, Optional, TYPE_CHECKING, cast

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
reveal_type(1)  # Revealed type is "builtins.int"

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing an explicit type annotation
x: list[str] = []
x: str | None = None

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = mystery_function()
# Mypy will let you do anything with x!
x.whatever() * x["you"] + x("want") - any(x) and all(x) is super  # no errors

# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to add a comment explaining the issue.
x = confusing_function()  # type: ignore  # confusing_function won't return None here because ...

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
a = [4]
b = cast(list[int], a)  # Passes fine
c = cast(list[str], a)  # Passes fine despite being a lie (no runtime check)
reveal_type(c)  # Revealed type is "builtins.list[builtins.str]"
print(c)  # Still prints [4] ... the object is not changed or casted at runtime

# Use "TYPE_CHECKING" if you want to have code that mypy can see but will not
# be executed at runtime (or to have code that mypy can't see)
if TYPE_CHECKING:
    import json
else:
    import orjson as json  # mypy is unaware of this

# In some cases type annotations can cause issues at runtime, see
# Annotation issues at runtime for dealing with this.

# See Silencing type errors for details on how to silence errors.
# Standard “duck types”

# In typical Python code, many functions that can take a list or a
# dict as an argument only need their argument to be somehow
# “list-like” or “dict-like”. A specific meaning of “list-like” or
# “dict-like” (or something-else-like) is called a “duck type”, and
# several duck types that are common in idiomatic Python are
# standardized.

# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def f(ints: Iterable[int]) -> list[str]:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""

    return [str(x) for x in ints]

f(range(1, 3))

# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = 'maybe'  # mypy will complain about this line...
    return list(my_mapping.keys())

f({3: 'yes', 4: 'no'})

def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
    my_mapping[5] = 'maybe'  # ...but mypy is OK with this.
    return set(my_mapping.values())

f({3: 'yes', 4: 'no'})

import sys
from typing import IO

# Use IO[str] or IO[bytes] for functions that should accept or return
# objects that come from an open() call (note that IO does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = 'w') -> IO[str]:
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
    if mode == 'w':
        return sys.stdout
    elif mode == 'r':
        return sys.stdin
    else:
        return sys.stdout

# You can even make your own duck types using Protocols and structural subtyping.
# Forward references

# You may want to reference a class before it is defined.
# This is known as a "forward reference".
def f(foo: A) -> int:  # This will fail at runtime with 'A' is not defined
    """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
    pass

# However, if you add the following special import:
from __future__ import annotations
# It will work at runtime and type checking will succeed as long as there
# is a class of that name later on in the file
def f(foo: A) -> int:  # Ok
    pass

# Another option is to just put the type in quotes
def f(foo: 'A') -> int:  # Also ok
    pass

class A:
    # This can also come up if you need to reference a class in a type
    # annotation inside the definition of that class
    @classmethod
    def create(cls) -> A:
        pass

# See Class name forward references for more details.
# Decorators

# Decorator functions can be expressed via generics. See Declaring
# decorators for more details. Example using Python 3.12 syntax:

from collections.abc import Iterator, Callable
from typing import Union, Optional

# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

# Coroutines and asyncio

# See Typing async/await for the full detail on typing coroutines and
#  asynchronous code.

import asyncio

# A coroutine is typed like a normal function
async def countdown(tag: str, count: int) -> str:
    while count > 0:
        print(f'T-minus {count} ({tag})')
        await asyncio.sleep(0.1)
        count -= 1
    return "Blastoff!"

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

class DataFrame(NDFrame, OpsMixin):
    """
    Two-dimensional, size-mutable, potentially heterogeneous tabular data.
    Data structure also contains labeled axes (rows and columns).
    Arithmetic operations align on both row and column labels. Can be
    thought of as a dict-like container for Series objects. The primary
    pandas data structure.
    Parameters
    ----------
    data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index.
        .. versionchanged:: 0.25.0
           If data is a list of dicts, column order follows insertion-order.
    index : Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided.
    columns : Index or array-like
        Column labels to use for resulting frame when data does not have them,
        defaulting to RangeIndex(0, 1, 2, ..., n). If data contains column labels,
        will perform column selection instead.
    dtype : dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer.
    copy : bool or None, default None
        Copy data from inputs.
        For dict data, the default of None behaves like ``copy=True``.  For DataFrame
        or 2d ndarray input, the default of None behaves like ``copy=False``.
        If data is a dict containing one or more Series (possibly of different dtypes),
        ``copy=False`` will ensure that these inputs are not copied.
        .. versionchanged:: 1.3.0
    See Also
    --------
    DataFrame.from_records : Constructor from tuples, also record arrays.
    DataFrame.from_dict : From dicts of Series, arrays, or dicts.
    read_csv : Read a comma-separated values (csv) file into DataFrame.
    read_table : Read general delimited file into DataFrame.
    read_clipboard : Read text from clipboard into DataFrame.
    Notes
    -----
    Please reference the :ref:`User Guide <basics.dataframe>` for more information.
    Examples
    --------
    Constructing DataFrame from a dictionary.
    >>> d = {'col1': [1, 2], 'col2': [3, 4]}
    >>> df = pd.DataFrame(data=d)
    >>> df
       col1  col2
    0     1     3
    1     2     4
    Notice that the inferred dtype is int64.
    >>> df.dtypes
    col1    int64
    col2    int64
    dtype: object
    To enforce a single dtype:
    >>> df = pd.DataFrame(data=d, dtype=np.int8)
    >>> df.dtypes
    col1    int8
    col2    int8
    dtype: object
    Constructing DataFrame from a dictionary including Series:
    >>> d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    >>> pd.DataFrame(data=d, index=[0, 1, 2, 3])
       col1  col2
    0     0   NaN
    1     1   NaN
    2     2   2.0
    3     3   3.0
    Constructing DataFrame from numpy ndarray:
    >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                        columns=['a', 'b', 'c'])
    >>> df2
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    Constructing DataFrame from a numpy ndarray that has labeled columns:
    >>> data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
                     dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
    >>> df3 = pd.DataFrame(data, columns=['c', 'a'])

    >>> df3
       c  a
    0  3  1
    1  6  4
    2  9  7
    Constructing DataFrame from dataclass:
    >>> from dataclasses import make_dataclass
    >>> Point = make_dataclass("Point", [("x", int), ("y", int)])
    >>> pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
       x  y
    0  0  0
    1  0  3
    2  2  3
    """
    pass
