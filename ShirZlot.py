#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:26:29 2019

@author: shirzlotnik
"""

def MakeDict():
    x=0
    dict={}
    for x in range (3):
        key = input("enter str:")
        val = int(input("enter num:"))
        dict[key]=val
    return dict

def CheckDict(dict1):
    str = input("enter str to check:")
    if str in dict1:
        print("Yes")
    else:
        print("No")
    return

def MakePowDict():
    dict={}
    for x in range(11):
        dict[x]=x**2
    return dict

dict1=MakeDict()
CheckDict(dict1)
dict2=MakePowDict()
print(dict2)
        
