def main():
    listNumOne = getWrit()
    listCount = getTotalNum(listNumOne)

    # print(getMax(listCount))
    print(getMin(listCount))

def getWrit():

    listNumOne = []
    listNum = []
    with open('pbnumbers.txt', 'r') as file:

        descr = file.readlines()
        for ch in descr:
            h = ch.split()
            listNum.append(h)

        for num in range(len(listNum)):
            for i in range(len(listNum[num])):
                topNum = listNum[num][i]
                listNumOne.append(topNum)
        return listNumOne

def getTotalNum(listNumOne):
    listCount = [0] * len(listNumOne)
    for ch in range(len(listNumOne)):
        count = 0
        for i in range(len(listNumOne)):
            if listNumOne[ch] == listNumOne[i]:
                count = count + 1
        listCount[ch] = count
    return listCount

def getMax(listCount):

    count = 0
    listMax = []
    totalVal = []
    resList = set(listCount)


    while count != 10:

        for i in resList:
            listMax.append(i)

        second_largest = listMax[0]
        largest_val = listMax[0]
        for i in range(len(listMax)):
            if listMax[i] > largest_val:
                largest_val = listMax[i]

        for i in range(len(listMax)):
            if listMax[i] > second_largest:
                second_largest = listMax[i]


        count = count + 1
        resList.remove(max(resList))
        listMax = []
        totalVal.append(second_largest)

    return totalVal


def getMin(listCount):

    count = 0
    listMax = []
    totalVal = []
    resList = set(listCount)


    while count != 10:

        for i in resList:
            listMax.append(i)

        second_largest = listMax[0]
        largest_val = listMax[0]
        for i in range(len(listMax)):
            if listMax[i] < largest_val:
                largest_val = listMax[i]

        for i in range(len(listMax)):
            if listMax[i] < second_largest:
                second_largest = listMax[i]


        count = count + 1
        resList.remove(min(resList))
        listMax = []
        totalVal.append(second_largest)

    return totalVal


if __name__ == "__main__":
    main()