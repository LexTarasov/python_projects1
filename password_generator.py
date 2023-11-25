import random

def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '%', '*', '^', '$', '|']
    numeros = ['1', '2', '3', '4', '5', '6', '7']

    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []
    
    for i in range(10):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password) 
    return password

def run():
  password = generar_password()
  print('tu nueva password es: ' + password)
  
  
if __name__=='__main__':
        run()