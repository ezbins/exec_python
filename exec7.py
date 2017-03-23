#!/usr/bin/env python3
# coding: utf-8

print("What is the length of the room in feet?", end=' ')
input_length = int(input())
print("What is width of the room in feet?", end=' ')
input_width = int(input())

print("You entered dimensions of {length} feet by {width} feet.".format(
    length=input_length, width=input_width), end='\n')


def cacl_square(length, width):
    square_feet = length * width
    square_meters = square_feet * 0.09290304

    return square_feet, square_meters


(square_f, square_m) = cacl_square(input_length, input_width)
print("The area is", end='\n')
print("{s_feet} square feet".format(s_feet=square_f), end='\n')
print("{s_meter} square meters".format(s_meter=square_m), end='\n')
