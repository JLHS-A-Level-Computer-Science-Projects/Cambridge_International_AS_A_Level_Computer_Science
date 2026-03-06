#Created by 4AMAlan

QueueArray = ['' for i in range(10)]     #global
HeadPointer = 0                          #global
TailPointer = 0                          #global
NumberOfItems = 0                        #global

def Enqueue(Queue, Head, Tail, NumOfItems, DataToAdd):
    if NumOfItems == 10:
        return False, Queue, Head, Tail, NumOfItems
    Queue[Tail] = DataToAdd
    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1
    NumOfItems += 1
    return True, Queue, Head, Tail, NumOfItems

def Dequeue(Queue, Head, Tail, NumOfItems):
    while NumOfItems > 0:
        ReturnValue = Queue[Head]
        Head += 1
        if Head >= 9:
            Head = 0
        NumOfItems -= 1
        return ReturnValue, Queue, Head, Tail, NumOfItems
    return False, Queue, Head, Tail, NumOfItems

for i in range(11):
    Data = input("Please input:")
    ReturnValue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Enqueue(QueueArray, HeadPointer, TailPointer, NumberOfItems, Data)
    if ReturnValue == True:
        print("Success")
    else:
        print("Queue is full.")

ReturnValue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print("First:", ReturnValue)
ReturnValue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print("Second:", ReturnValue)