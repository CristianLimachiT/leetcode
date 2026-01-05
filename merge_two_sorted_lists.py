class Solution:
    def mergeTwoLists(list1, list2):
        list1.extend(list2)
        list1.sort()

        return list1
    list1 = [1,2,9]
    list2 = [1,3,6]

    salida = mergeTwoLists(list1,list2)
    print(salida)
