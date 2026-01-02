#class Solution:
def twoSum(nums, target):
    
    for i in range(len(nums)): 
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    salida = [i,j]
                    return(salida)
nums = [1,3,2,6,9]
lista_salida = twoSum(nums, 9)

print('lista salida:', lista_salida)
