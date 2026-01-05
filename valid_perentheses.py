# el ejercicio consiste en que el string que contenga la funcion, sea 
# {}, (), [], deben contener los dos simbolos y en el orden mostrado

class Solution:
    def isValid(s):
        
        tupla = ('{','}','(',')','[',']')
        pos = 0
        
        for i in s:
            if i not in tupla:
                return False

            pos += 1
            cont = 0
            pos_fin = 0
            
            if i != ')' and i != '}' and i != ']':
                if (i == '{' and '}' in s) or (i == '[' and ']' in s) or (i == '(' and ')' in s):
                    for j in range(pos,len(s)):
                        cont += 1
                        if i == '{' and s[j] == '}':
                            pos_fin= cont
                            #print('termino bien' if pos_fin%2 == 1 else 'termino mal')
                            return True if pos_fin%2 == 1 else False
                        elif i == '(' and s[j] == ')':
                            pos_fin= cont
                            return True if pos_fin%2 == 1 else False
                        elif i == '[' and s[j] == ']':
                            pos_fin= cont
                            return True if pos_fin%2 == 1 else False
                else:
                    return False
                    #print('simbolo ingresado no tiene fin :',i)
            elif (i == '}' and '{' not in s) or (i == ']' and '[' not in s) or (i == ')' and '(' not in s):
                return False
                #print('simbolo ingresado no tiene inicio :',i)

    entrada = '(){}}{'
    salida = isValid(entrada)
    print(salida)


