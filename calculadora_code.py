#Funciones con opeariones basicas

def sumar(a, b):
    return a + b 
def restar(a, b):
    return a - b 
def multiplicar(a, b):
    return a * b 
def dividir(a, b):
    if b == 0: 
        raise ValueError("No se puede dividir por cero.") 
    return a / b

#Funcion ppal Calculadora
def calculadora():
    #Menu interactivo
    print("\n *** CALCULADORA ***")
    a = float(input("Ingresa el primer numero: ")) 
    b = float(input("Ingresa el segundo numero: "))
    print("1. Sumar, 2. Restar, 3. Mult, 4. Div")
    opcion = input("Por favor ingresa una opcion entre (1 - 4): ")
    #Bloque de codigo para el control de errores con try-except.
    try:
        
        if(opcion == "1"): resultado = sumar(a, b)
        elif(opcion == "2"): resultado = restar(a, b) 
        elif(opcion == "3"): resultado = multiplicar(a, b) 
        elif(opcion == "4"): resultado = dividir(a, b) 
        else:
            print("Opcion invalida")
            return
        print(f"El resultado es: {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")
#instruccion obligatoria de cierre del bloque de la funcion        
if __name__ == '__main__':
    calculadora()
 
"""
Tipos de excepciones comunes:
● ZeroDivisionError
● ValueError
● KeyError

"""
