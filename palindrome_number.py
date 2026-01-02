#consigna: ingresar un numero entero y 
#          devolver en boleano si es palindromo o no
class Solution:
    def isPalindrome(x):
        # convertimos el integer en string para convertirlo en una lista
        list_str = str(x)
        # convertimos el string en lista
        list_ordenada = list(list_str)
        # generamos la lista invertida vacia
        list_invertida = []

        # bucle que va desde el ultimo elemento hasta el primero 
        # en reversa, por cada elemento agrega en la lista invertida
        for i in range((len(list_ordenada)-1),-1,-1):
            list_invertida.append(list_ordenada[i])

        # evaluamos si la lista invertida esta ordenada, si no lo esta
        # devolvemos false 
        if list_ordenada == list_invertida:
            return True
        else: 
            return False

    salida = isPalindrome(1111)
    print(salida)