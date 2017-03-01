import random

def bubblesort(List):
    listLength = len(List)-1
    for outer in range(0,listLength):
        for inner in range(0, listLength):
            if List[inner] > List[inner+1]:
                temp = List[inner]
                List[inner] = List[inner+1]
                List[inner+1] = temp
                print(List)
        listLength = listLength - 1


numbers = []
maxLengthList = int(input("How many number do you want to sort?: "))
while len(numbers) < maxLengthList:
    number = int(input("Enter the number you want to sort: "))
    numbers.append(number)
    print(numbers)
bubblesort(numbers)

