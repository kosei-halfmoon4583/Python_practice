#!/usr/bin/env python
# __coding: UTF-8 __

# for test 2023/9/20 by NAOSHI Watanuki.
import math
from unittest import result

# for test of VS code 2023/9/10(Sun.)
class Dog:
    name = ""
    def bark(self):
        m = self.name + ": Bow-wow!"
        print(m)

pochi = Dog()
pochi.name = "Pochi"
pochi.bark()

hachi = Dog()
hachi.name = "Hachi"
hachi.bark()
