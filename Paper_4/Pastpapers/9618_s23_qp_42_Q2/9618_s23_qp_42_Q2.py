#Created by 4AMAlan

class SaleData:
    def __init__(self, i, q):
        self.id = i                #type: STRING
        self.quantity = q          #type: INTEGER

CircularQueue = [SaleData("", -1) for i in range(5)]      #global
Head = 0                                                  #global
Tail = 0                                                  #global
NumberOfItems = 0                                         #global

def Enqueue(NewRecord) -> int:
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems > 4:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        if Tail == 4:
            Tail = 0
        else:
            Tail += 1
    NumberOfItems += 1
    return 1

def Dequeue() -> SaleData:
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        FirstRecord = SaleData("", -1)
    else:
        FirstRecord = CircularQueue[Head]
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        else:
            Head += 1
    return FirstRecord

def EnterRecord(id, quantity):
    ReturnValue = Enqueue(SaleData(id, quantity))
    if ReturnValue == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5)
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3)

ReturnValue = Dequeue()
if ReturnValue.id == "":
    print("The queue is empty.")
else:
    print(ReturnValue.id)

print()

EnterRecord("LLP", 3)

for i in range(5):
    print(CircularQueue[i].id, end = " ")
    print(CircularQueue[i].quantity)