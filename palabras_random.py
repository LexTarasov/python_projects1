'''
adj = input('ingresa un adjetivo> ')
verbo1 = input('verbo1> ')
verbo2 = input('verbo2> ')
sustantivo = input('sust plural> ')

madlib = f"La vida es muy {adj} y lo que mas me gusta hacer con ella es {verbo1} y despues {verbo2} con mi {sustantivo}"

print(madlib)'''

#adivina el numero
import random
def adivina_el_numero(x):
   print('*******************************')
   print('Bienvenido a adivina el numero')
   print('*******************************')
   print('tu meta es adivinar el numero q elige la pc')

   numero_pc = random.randint(1, x) 

   num_usuario = 0

   while num_usuario != numero_pc:
    num_usuario = int(input(f'ingresa el numero entre 1 y {x}>> '))
    if num_usuario < numero_pc:
     print('el numero que ingresaste es menor')
    elif num_usuario > numero_pc:
     print('el numero que ingresaste es mayor')
    else:
     print(f'FELICIDADES adivinaste el numero era {numero_pc}')   


adivina_el_numero(20)