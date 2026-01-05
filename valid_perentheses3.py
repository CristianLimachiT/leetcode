# el ejercicio consiste en que el string que contenga la funcion, sea 
# {}, (), [], deben contener los dos simbolos y en el orden mostrado

class Solution:
    def isValid(s):
        # generamos el diccionario que asocia el simbolo cierre con el simbolo inicio 
        dic = {'}': '{',')': '(',']': '['}
        # generamos una lista con funcion de stack, esto nos sirve para que poder accederlo como ultimo 
        # elemento de la lista
        stack = []

        flag_final = False
        # si el string no es par significa que hay algun simbolo suelto, por lo que cancelamos la funcion
        if len(s)%2 == 1:
            return flag_final

        for i in s:
            # evaluamos si el simbolo es en dic
            if i in dic:
                # si stack no esta vacio, y el ultimo elemento del stack matchea con el que estamos viendo
                # ejemplo: stack[-1] = '(' y dic[i] = '('
                if stack != [] and stack[-1] == dic[i]:
                    # eliminacmos el ultimo elemento del stack
                    stack.pop()
                else:
                # si el ultimo elemento del stakc no matchea, por ejemplo :stack[-1] = '[' y dic[i] = '('
                # terminamos la funcion
                    flag_final = False 
                    return flag_final 
            # si no esta en dic, lo agregamos al stack    
            else:
                stack.append(i)      

        if stack == []:
            flag_final = True
            return flag_final
        else:
            flag_final = False
            return flag_final
        
    entrada = '([)]'
    salida = isValid(entrada)
    print(salida)