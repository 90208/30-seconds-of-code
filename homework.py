# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:09:57 2020

@author: cis-user
"""

print("解一元二次方程式")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
y=(b**2)-(4*a*c)
x1=(-b+(y**0.5))/(a*2)
x2=(-b-(y**0.5))/(a*2)
print(x1,x2)