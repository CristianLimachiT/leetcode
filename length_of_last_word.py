class Solution:
    def lengthOfLastWord(s):
        # el metodo split() nos convierte un strin en una lista separada por el parametro que le pasemos,
        # en este caso le pasamos que divida por espacios
        lista = s.split(' ')

        i = -1
        # usamos la variable ultima para tomar el ultimo componente de la lista
        ultima = lista[i]

        # mientras el ultimo componente de la lista no sea un espacio en blanco, seguimos buscando el siguiente
        while ultima == '':
            i -= 1
            ultima = lista[i]

        return len(ultima)
    
    entrada = 'Hello World'
    salida = lengthOfLastWord(entrada)
    print(salida)