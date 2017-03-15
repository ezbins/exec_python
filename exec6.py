#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime

print("What is your current age?", end=' ')
input_age = int(input())
print("At what age would you like to retire?", end=' ')
input_retire_age = int(input())

current_year = datetime.now().year
gap = input_retire_age - input_age
print("You have {gap} years left until you can retire.".format(
    gap=gap))
print("It's {current_year},so you can retire in {feature_year}".format(
    current_year=current_year, feature_year=current_year + gap), end='\n')
