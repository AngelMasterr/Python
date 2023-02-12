# Programa Python para mostrar la secuencia de Fibonacci
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-2) + recur_fibo(n-1))

nterms = 10

# verificar si el número de términos es válido
if nterms <= 0:
    print("Por favor, introduzca un entero positivo")
else:
    print("Secuencia de Fibonacci:")
    for i in range(nterms):
        print(recur_fibo(i))