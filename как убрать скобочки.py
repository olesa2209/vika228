# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:21:11 2023

@author: Pupil
"""
# a='текст текст текст (текстик) текст'
# b='(текстик)'
# def Vika(a,b):
#     c=a.find(b)
#     print(c)
#     if c!=-1:
#         v=a.replace(b,'')
#         print(v)
#     else: 
#         print('ghffjhj')
# Vika(a,b)

a='ntlfjf(hfhfh)ура(jgjgjgjg) ура(gfjfb) ура'
def Vika2(a):
    w=a.count('(')
    for i in range(w):
        c=a.find('(')
        s=a.find(')')
        v=a[:c]+a[s+1:]
    print(v)
Vika2(a)