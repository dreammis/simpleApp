# def select_sort(arr):
#
#     for i in range(len(arr)-1,-1,-1):
#         select_one = len(arr)-i-1
#         for j in range(i+1):
#
#             if arr[select_one]>arr[j]:
#                 select_one = j
#         arr[i],arr[select_one] = arr[select_one],arr[i]
#
#     return arr
# l= [12,5,3,6,15]
# print select_sort(l)















def select_sort(arr):

    index = 0

    while index!=(len(arr)-1):
        choose = index

        for i in range(index,len(arr)):
            if arr[choose]>arr[i]:choose = i
        arr[index],arr[choose] = arr[choose],arr[index]
        index +=1

    return arr
l= [12,5,3,6,15]
print select_sort(l)














