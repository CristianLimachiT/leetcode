class Solution:
    def mySqrt(x):
        a = 1
        while x >= a*a:
            a += 1

        salida = a - 1
        return salida 
        
    entrada = 22222222
    resultado = mySqrt(entrada)
    print(resultado)