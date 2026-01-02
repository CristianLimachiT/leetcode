# ejercicio para devolver los prefijos comunes en los caracteres de una cadena

class Solution:
    def longestCommonPrefix(strs):
        #string de salida
        string_salida = ''
        #flag para indicar si se graba el string para la salida
        no_write = 0
        #de los componentes de strs toma el mas chico para hacer el for
        #de lo contrario da un error de index
        min_len = min(len(s) for s in strs)

        #ciclo for hasta el largo de la cadena mas chica
        for i in range(min_len):
            letra_anterior = ' '
            for s in strs:
                # evalua si la letra anterior no es igual a la de ahora setea
                # no grabar el string
                if s[i] != letra_anterior and letra_anterior != ' ':
                    no_write = 1
                letra_anterior = s[i]
            # si no se indico no grabar se graba
            if no_write != 1:
                string_salida += s[i]
        # devolvemos el string de salida
        return string_salida

                
    entrada = ["a","aavv","aav"]
    salida = longestCommonPrefix(entrada)

    print(salida)