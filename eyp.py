#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Blah blub: just a playground. """

import os
# import pdb
# import random
# import re
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

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        """mypy will infer the correct types for these instance variables
         based on the types of the parameters."""
        self.account_name = account_name
        self.balance = initial_balance
        
    class Asdf():
        """Asdf. """
        def __init__(self, title, author, price, zeit=time.strftime('%Y%m%d--%H-%M-%S')):
            self._title = title
            self._author = author
            self._price = price
            self.zeit = zeit

        @property
        def zeit(self):
            """Asdf. """
            print(self.zeit)
            return self.zeit

        @property
        def title(self):
            """Asdf. """
            print(self._title)
            return self._title

        @property
        def author(self):
            """Asdf. """
            return self._author

        @property
        def price(self):
            """Asdf. """
            return self._price

        @price.setter
        def price(self, price):
            """Asdf. """
            if price >= 0:
                self._price = price
            else:
                raise ValueError("Price cannot be negative")

        # def Utf8_exists(filename) -> a[1:2]:
        # def utf8_exists(self, filename):
        #     """Asdf. """
        #     return os.path.exists(filename.encode('utf-8'))

        def utf8_exists(self, filename: str) -> bool:
            """Check if file exists and can be read as UTF-8."""
            print(self.zeit)
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    f.read()
                return os.path.exists(filename)
            except (FileNotFoundError, UnicodeDecodeError):
                return False

        def foo1(self):
            """Asdf. """
            print('foo1')

