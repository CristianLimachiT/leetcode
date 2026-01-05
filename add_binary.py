class Solution:
    def addBinary(a, b):
        #int1 e int2 son los valores de string convertidos a decimal, esto se hace mediante
        # el segundo parametro, que le indicamos que el string esta en base 2, osea binario
        int1 = int(a,2)
        int2 = int(b,2)
        # intout seria la suma de int1 + int2 convertido a binario
        intout = bin(int1 + int2)
        # strout nos convierte intout en un string
        strout = str(intout)
        # es importante devolver la salida desde la posicion 2 porque en binario devuelve
        # los primeros dos digitos con informacion de bin
        return strout[2:]
        
    entrada1 = '1010'
    entrada2 = '1011'

    salida = addBinary(entrada1,entrada2)
    print(salida)
    print(type(salida))