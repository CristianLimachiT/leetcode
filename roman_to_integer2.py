class Solution:
    def romanToInt(self, s: str) -> int:
        #diccionario con los valores en numeros romanos e integer
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" :1000 }

        entrada = list(s)

        def f_validador(entradaf):
    
            simbolo_aux = entradaf[0]
            contador = 0
    
            for z in entradaf:
                if z == simbolo_aux:
                    simbolo_aux = z
                    contador += 1
                    if contador >= 4:
                        return(1)
                else:
                    simbolo_aux = z
                    contador = 1
                    return(0)
        
        def f_conversor(entradaf):
    
            sum_salida = 0  
            num_anterior = 0
    
            for i in entradaf:
                for j in dic: 
                    if j == i:
                        # validador de numero
                        if dic[j] <= num_anterior or num_anterior == 0:
                            sum_salida += dic[j]
                        elif dic[j] > num_anterior and num_anterior != 0:
                            sum_salida -= num_anterior
                            sum_salida += dic[j] - num_anterior
                        num_anterior = dic[j]
            return sum_salida
        
        validacion = f_validador(entrada)

        if validacion != 1:
            salida = f_conversor(entrada)
            print('el numero en entero seria FINAL :', salida)
            return(salida)   
        else:
            print('el numero ingresado es erroneo')    

