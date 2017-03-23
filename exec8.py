#!/usr/bin/env python3
# coding: utf-8

import sys


def checkNumber(value):
    if value.isnumeric():
        return int(value)
    else:
        print("Please input number.")
        sys.exit()


print("How many people?", end=' ')
input_people = input()
people = checkNumber(input_people)

print("How many pizzas do you have?", end=' ')
input_pizza = input()
pizza = checkNumber(input_pizza)

leftover = people % pizza

print("{people} people with {pizza} pizzas".format(
    people=input_people, pizza=input_pizza), end='\n')
print("Each person gets {pices} pieces of pizza.".format(
    pices=input_pizza), end='\n')
print("There are {leftover} leftover pieces.".format(
    leftover=leftover), end='\n')
