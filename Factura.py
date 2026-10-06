# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:30:55 2026

@author: Gonzalo
"""

miPrecio = float(input('Precio del producto: '))
misUnidades = int(input('Nº de unidades: '))

miSubtotal = miPrecio * misUnidades
miIVA = miSubtotal * 0.21
miTotal = miSubtotal + miIVA

print('----- FACTURA -----')
print(f'Precio unidad: {miPrecio:.2f}')
print(f'Unidades: {misUnidades}')
print(f'subtotal: {miSubtotal:.2f} €')
print(f'IVA: {miIVA:.2f} €')
print(f'Total: {miTotal:,.2f} €')