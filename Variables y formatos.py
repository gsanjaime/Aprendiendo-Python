import sys
print(sys.executable)

miNombre = "Gonzalo"
miEdad = 54
miAltura = 1.80

miNombre2 = "Marcos"
miEdad2 = 18
miAltura2 = 1.80


print('la variable miNombre es de tipo',type(miNombre))
print('la variable miEdad es de tipo',type(miEdad))
print('la variable miAltura es de tipo',type(miAltura))

print ('Me llamo',miNombre)
print ('Tengo',str(miEdad),'años')
print (f'Mido {miAltura:.2f} metros')
print ('El año que viene tendré',str(miEdad+1),'años')
print (f'Mi edad es {miEdad:-<10}')
print (f'Mi edad es {miEdad:>10.2f}')
print (f'Mi edad es {miEdad:0^10.2f}')


print(f'{'Nombre':<10} {'Edad':>10} {'Altura':>10}')
print(f'{'-'*33}')
print(f'{miNombre:<10} {miEdad:>10} {miAltura:>10}')
print(f'{miNombre2:<10} {miEdad2:>10} {miAltura2:>10}')
 



