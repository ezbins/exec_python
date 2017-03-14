#!/usr/bin/env python3
# coding: utf-8
import sys

print("What is the input string?", end=' ')
input_name = input()
if not input_name:
    print("Input some string!!")
    sys.exit()
else:
    print("{name} has {length} characters.".format(
        name=input_name, length=len(input_name)))
