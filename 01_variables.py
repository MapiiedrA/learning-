# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion De Variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas Funciones del Sistema #Len()= cuenta el numero de caracteres de una cadena
print(len(my_string_variable)) 

#Variables en una sola linea #el orden del print no afecta el resultado solo el orden #Nombre y alias son Cadenas de Texto y la edad un entero(no es necesario la comillas) #Cuidado en otros lenguajes puede ser brujeria! no abusar de esta syntaxis
name, surname, alias, Age = "Mauricio" , "Piedra", "MapiiedrA" , 32
print("me llamo:", name, surname, "y mi alias es:", alias, "mi edad es:", Age, "años")  

#Sistema de input (poco Habitual) puede completarse en la terminal si requiere datos y los agrega (como scripts o programas trabajan desde la terminal)
name = input('¿Cual es tu nombre?: ')
age = input('¿Cual es tu edad?: ')

print(name)
print(age)

#Solo Pruebas! Cambiamos su tipo (reasignacion de Variable)
"""
name = 32
age = "Mauricio"

print(name)
print(age)  
"""

#Forzamos el tipo de dato de una variable (casting) (si se agregan varios type solo se queda con el ultimo)
address: str = "Mi direccion:"
address = 32
print(type(address))


