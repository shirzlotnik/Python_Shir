#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:17:49 2019

@author: shirzlotnik
"""

def Sort_DK():
    di={"shir":7,"Jacob":10}
    for x in sorted(di.keys()):
        print(x,di[x])
        
def Sort_DV():
    di={"shir":7,"Jacob":10}
    for x,y in sorted(di.items(),key=lambda item: item[1]):
        print(x,y)
        
Sort_DK()
Sort_DV()
        

