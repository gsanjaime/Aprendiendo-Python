# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:32:40 2026

@author: Gonzalo
"""

miNota = int(input('Introduce la nota: '))

if miNota <5:
    print('Suspenso')
elif miNota < 7:
    print('Aprobado')
elif miNota < 9:
    print('Notable')
elif miNota < 10:
    print('Sobresaliente')
elif miNota == 10:
    print('Matrícula de Honor')
else:
    print('Nota incorrecta')    

    