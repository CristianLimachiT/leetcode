
# el ejercicio consiste en que el string que contenga la funcion, sea 
# {}, (), [], deben contener los dos simbolos y en el orden mostrado

class Solution:
    def isValid(s):
        
        #dic = {'{': '}','(': ')','[': ']'}
        #pos_fin = 0
        flag = False
        if len(s)%2 == 1:
            return flag
  
        flag_ini = False
        for i in range(0,len(s)):
            #flag_ini = False
            if s[i] != ')' and s[i] != '}' and s[i] != ']':
                flag_ini = True
                #print('s[i]',s[i])
                pos_fin = 0
                flag = False
                for j in range(i+1,len(s)):
                    #print('check s[j]',s[j])
                    pos_fin += 1
   
                    if s[i] == '{' and s[j] == '}':
                        #return True if pos_fin%2 == 1 else False
                        if pos_fin%2 == 1:
                        #    print('s[j]',s[i],s[j])
                            flag = True
                            break
                        else:
                            flag = False 
                            return flag 
                    if s[i] == '[' and s[j] == ']':
                        #return True if pos_fin%2 == 1 else False
                        if pos_fin%2 == 1:                                  
                            #print('s[j]',s[j])
                            flag = True
                            break
                        else:
                            flag = False 
                            return flag 
                    if s[i] == '(' and s[j] == ')':
                        #return True if pos_fin%2 == 1 else False
                        #print('no pasamos por aca?')
                        if pos_fin%2 == 1:
                            #print('s[j]',s[j])
                            flag = True
                            break
                        else:
                            #print('hicimos false')
                            flag = False
                            return flag 
                    #if flag == False:
                    #    print('pasamos por aca',s[i],s[j])
                        #flag = False
                        
                    #    return flag
            else:
                if flag_ini == False or flag != True:
                    flag = False
                    return flag
                    #print('else :' ,s[i])
        return(flag)                
                #else:
                #    print('fallo s[j]:', s[j])
               

    #entrada = '([]'
    #entrada = '()'
    #entrada = '()[]{}'
    #entrada = '(]'
    #entrada = '([])'
    entrada = '([}}])'
    salida = isValid(entrada)
    print(salida)
