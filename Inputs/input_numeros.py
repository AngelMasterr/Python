# input : pedirle un dato al usuario y siempre sera string
numero = input("introduzca el número: ")
print(numero)

# multiplicar numeros, como es un string lo que hace es duplicar el valor la cantidad de veces dada (no multiplica)
resultado = numero * 2
print(resultado)

# para poder multiplicar es necesario convertir el valor a numero (int o float)
resultado_2 = float(numero) * 2 # puede ser entero o decimal, si introduzco texto sale error
print(resultado_2)

resultado_3 = int(numero) * 2 # tiene que ser un valor entero, si introduzco un decimal o texto sale error
print(resultado_3)

