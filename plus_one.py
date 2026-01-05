class Solution:
    def plusOne(digits):
        #stack = []
        s = str(digits)

        i = -1
        ultima = digits[i]

        while ultima == 9:
            digits.pop()
            if digits != []:
                digits[-1] = digits[-1] + 1
                digits.append(0)
            else:
                digits.append(1)
                digits.append(0)
            

            i -= 1
            ultima = digits[i]
            print(ultima)
            
        return digits
    
    entrada = [9,9]
    salida = plusOne(entrada)
    print(salida)