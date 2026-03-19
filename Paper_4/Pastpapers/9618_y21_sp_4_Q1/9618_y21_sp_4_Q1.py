#Created by 4AMAlan

TheData = [20,3,4,8,12,99,4,26,4]

def InsertionSort(TheData):
    for i in range(len(TheData)):
        DataToInsert = TheData[i]
        Inserted = 0
        NextValue = i - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for i in range(len(TheData)):
        print(TheData[i], end = " ")

def LinearSearch():
    global TheData
    NumberToSearch = int(input("Please input a number:"))
    for i in range(len(TheData)):
        if TheData[i] == NumberToSearch:
            print("Found")
            return True
    print("Not Found")
    return False

print("Before Sort")
PrintArray(TheData)
InsertionSort(TheData)
print()
print("After Sort")
PrintArray(TheData)
print()

LinearSearch()