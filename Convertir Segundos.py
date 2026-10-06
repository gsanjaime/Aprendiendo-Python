# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:45:05 2026

@author: Gonzalo
"""

totalSegundos = int(input('Introduce los segundos:'))
misSegundos = totalSegundos % 60


print(f'Total Segundos: {totalSegundos} ')
print(f'Mis Segundos: {misSegundos} ')

totalMinutos = totalSegundos // 60
misMinutos = totalMinutos % 60
print(f'Total Minutos: {totalMinutos} ')
print(f'Mis Minutos: {misMinutos} ')

totalHoras = totalMinutos // 60
print(f'Total Horas: {totalHoras} ')


print(f'\n{totalSegundos} segundos son:')
print(f'{totalHoras} horas')
print(f'{misMinutos} minutos')
print(f'{misSegundos} segundos')