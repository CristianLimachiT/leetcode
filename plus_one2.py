class Solution:
    def plusOne(digits):
        # generamos un string donde vamos poner los int de digits    
        s = ''

        for i in digits:
            # dentro del string vaciom agregamos cada valor de digits en formato string
            s += str(i)

        # transformamos el string en un entero para hacer la operacion de +1
        entero = int(s)
        entero += 1

        # generamos s2 para volver a transformar el entero en un string
        s2 = str(entero)
        
        # generamos la lista vacia
        lista = []
        
        # como haciendo la conversion de list(s2) nos deja los componentes de adentro como string y se
        # requiere que sean integer, vamos a iterar por cada elemento, los transformamos a integer
        # y lo agregamos a la lista
        for j in s2:
            lista.append(int(j))
        return lista
    
    entrada = [9,9]
    salida = plusOne(entrada)
    print(salida)
