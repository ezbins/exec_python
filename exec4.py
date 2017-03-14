#!/usr/bin/env python3
# coding: utf-8

print("Enter a noun:", end=' ')
input_noun = input()
print("Enter a verb:", end=' ')
input_verb = input()
print("Enter a adjective:", end=' ')
input_adj = input()
print("Enter a adverb:", end=' ')
input_adv = input()

print("Do you {verb} your {adj} {noun} {adv}? This's hilarious!".format(
    verb=input_verb, adj=input_adj, noun=input_noun, adv=input_adv))
