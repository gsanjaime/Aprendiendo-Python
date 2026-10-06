# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:03:30 2026

@author: Gonzalo
"""


divisible_4 = False
no_divisible_100  = False
divisible_400  = False


mianyo = int(input('Introduce año: '))
if (mianyo % 4) == 0:    
   divisible_4 = True
   
if (mianyo % 100) != 0: 
    no_divisible_100  = True

if (mianyo % 400) == 0:
    divisible_400  = True

        
if divisible_4: 
    if no_divisible_100:
        print('Año bisiesto')        
    else:        
        if divisible_400:
            print('Año bisiesto')
        else:
            print('Año no bisiesto')
else:
        print('Año no bisiesto')


if divisible_4 and no_divisible_100:
    print('Año bisiesto')        
elif divisible_400:
    print('Año bisiesto')
else:
    print('Año no bisiesto')
