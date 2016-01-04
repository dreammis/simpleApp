
def maoPaoPai(lt):
    for i in range(len(lt)-1,-1,-1):
        for j in range(i):
            temp = None
            if lt[j]>lt[j+1]:
                temp = lt[j]
                lt[j] = lt[j+1]
                lt[j+1] = temp
    return lt

def selectPai(lt):

    for i in range(len(lt)-1,-1,-1):
        element = lt[len(lt)-1-i]
        temp = None
        index = len(lt)-1-i
        for j in range(len(lt)-1-i,i):
            if element>lt[j+1]:
                element = lt[j+1]
                index = j+1
        temp = lt[len(lt)-1-i]
        lt[len(lt)-1-i] = element
        lt[index] = temp
    return lt

def insertPai(lt):
    sortedList = []
    for i in range(len(lt)-1):
        sortedList.append(lt[i])
        index = -1
        for j in range(len(sortedList)-1):
            if sortedList[-2-j]>sortedList[index]:
                sortedList[-2-j],sortedList[index] = sortedList[index],sortedList[-2-j]
                index = -2-j
    return sortedList






lt = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

print insertPai(lt)