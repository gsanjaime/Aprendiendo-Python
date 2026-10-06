# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:25:02 2026

@author: Gonzalo
"""

miTemperatura = int(input('Introduce la temperatura: '))
if miTemperatura < 0:
    print('Hace mucho frío')
elif miTemperatura <15:
    print('Hace frío')
elif miTemperatura <25:    
    print('Temperatura agradable')
else:
    print('Hace calor')

    