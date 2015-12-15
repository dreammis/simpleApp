def selectSort(arr):
    for i in range(len(arr)-1,-1,-1):
        tem = ''
        index = len(arr)-1-i
        for j in range(len(arr)-1-i,i):
            if arr[index]>arr[j+1]:
                index = j+1
        tem = arr[index]
        arr[index] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = tem
    return arr

def maopaoSort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                tem = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tem

    return arr

a = [1,23,543,634,23633322,442,5,1534,2,45]
print selectSort(a)

