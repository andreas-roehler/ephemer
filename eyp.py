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

# def usage():
#     """Print Fehler. """
#     print("""Fehler: %s
# Es muß die aufzurufende Ziehungszahl als Argument angegeben werden:
# 'python roulette.py 1, 'python roulette.py 2', ... 'python roulette.py n'.
# """ % (
#           os.path.basename(sys.argv[0])))

def main():
    """Some main. """
    # if len(sys.argv) == 1:
    #     usage()
        # sys.exit()

    # def __init__(self, account_name: str, initial_balance: int = 0) -> None:
    #     """mypy will infer the correct types for these instance variables
    #      based on the types of the parameters."""
    #     self.account_name = account_name
    #     self.balance = initial_balance

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

    aaa = Asdf.zeit
    print(aaa)
    Asdf.foo1('')

    # >>> main()
    # <property object at 0x7254b1d47dd0>
    # foo1

# pdb.set_trace()
try:
    Anzahl = int(args[1])
except:
    print("Setze Anzahl auf 1")
    Anzahl = 1

# class Kugel() -> a[1:2]:
class Kugel():
    """Class Kugel. """
    zeitT = time.strftime('%Y%m%d--%H-%M-%S')
    # zeitT = time.strftime('%Y-%m-%d--%H-%M-%S')
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

zeitT = Kugel.zeitT
ausgabeE = Kugel.ausgabe
spiel = Kugel.spiel
gruen = Kugel.gruen
rot = Kugel.rot
schwarz = Kugel.schwarz
trefferR = Kugel.treffer
fertigG = Kugel.fertig

klauf = Kugel()

# with file("roulette-" + zeitT + ".csv", 'w') as datei:
#     for i in range(Anzahl):
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
# inst.a, inst.b, inst.c = 'foo', 'bar', 'baz'
(a, b, *c, d) = x, *y = 5, 6, 7, 8, 9

print('%(language)s has %(number)03d quote types.' %
       {'language': "Python", "number": 2})

print("%(language)s has %(number)03d quote types." %
       {'language': "Python", "number": 4})

# (long, sequence, of_items,
#     that, needs, to_be, wrapped) = input_list

if __name__ == "__main__":
    main()
