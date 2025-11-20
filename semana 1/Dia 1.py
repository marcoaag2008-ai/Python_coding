String = "Hola"
Int = 2                    #Cada variable tiene un nombre y valor que puede ser modificado
floats = 2.4
bools = True or False      #eso se conoce como tipado dinamico      

print(type(String)) # <Class "int">

input #Pedir e interactuar con usuario, devuelve unicamente strings                           

###OPERACIONES BASICAS###

a = 10
b = 3

print(a + b)   # 13
print(a - b)
print(a * b)
print(a / b)   # división normal (float)
print(a // b)  # división entera → 3
print(a % b)   # módulo → 1
print(a ** b)  # potencia → 1000

###CASTING###

edad = int("18")          
altura = float("1.78")   #Converison de tipos de datos, si intentas convertir algo no convertible: error

#/////////////////TIPS//////////////////////

#1.Saber si un string es un numero
Contador = "123124"
print(Contador.isdigit) # True

#2.Validacion basica

try:
    Peticion = int(input("Ingrese edad : "))
    print("EDAD VALIDA", Peticion)

except ValueError:
    print("Ingrese un valor de edad valido")

#.3.Decimales limpios

Numeros = 10/3
print(round(Numeros,4)) #round(numero, cantidad de decimales):3.3333

#4.F-strings con expresiones

Nombre_Usuario = "Camilo"
print(f"Hola {Nombre_Usuario} bienvenido")

#5.Operador Walrus(permite asigar durante una comparacion)

if(n:=5)>3:
    print(n)# 5

###MINI PROYECTO###
print("----------------------------------")
print("########### Aplicacion ###########")
print("----------------------------------")

Nombre_Usuario = input("Ingresa tu nombre de usuario : ").strip()

try:
    Edad_Usuario = int(input("Ingresa tu edad : "))
except ValueError:
    print("Ingresar valor de edad valido(entero)")

try:
    Altura_Usuario = float(input("Ingresa tu altura: "))
except ValueError:
    print("Ingresar valor de altura valido")

Calculo_Edad = 30 - Edad_Usuario
Calculo_Altura = Altura_Usuario * 100

if Calculo_Edad < 0:
    print(f"{Nombre_Usuario} tienes {Edad_Usuario} años, eso significa que ya haz alcanzado los 30, ademas mides {Calculo_Altura}cm ")
else:
    print(f"{Nombre_Usuario} te faltan {Calculo_Edad} años para cumplir 30, ademas mides {Calculo_Altura} cm")

if Altura_Usuario >= 1.80:
    print("Felicidades, eres realmente alto")    
else:
    print("Tienes una altura promedio")    
while True:

    Pregunta_IMC = input("¿Le gustaria que calculemos su IMC? (Si/No) : ").strip()
    if Pregunta_IMC.lower() == "no":
         print("Esta bien, para la proxima :D")
         break
    elif Pregunta_IMC.lower() == "si":
         try:
             Peso_Usuario = float(input("Ingrese su peso(kg) : ")) 
             Calcular_IMC = Peso_Usuario / Altura_Usuario ** 2
             print(f"Tiene un IMC de {round(Calcular_IMC,2)}")
             break
         except ValueError:
             print("Ingresar un valor de peso valido")
          
    else:
        print("Responda (Si/No)")