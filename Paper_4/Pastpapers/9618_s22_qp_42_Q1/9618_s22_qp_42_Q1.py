#Created by 4AMAlan

StackData = [0 for i in range(10)]  #global
StackPointer = 0                    #global

def output():
    global StackData, StackPointer
    print(StackPointer)
    for i in range(10):
        print(StackData[i])

def Push(In):
    global StackData, StackPointer
    while StackPointer < 10:
        StackData[StackPointer] = In
        StackPointer += 1
        return True
    return False

def Pop():
    global StackData, StackPointer
    StackPointer -= 1
    while StackPointer > -1:
        Popped = StackData[StackPointer]
        StackPointer -= 1
        return Popped
    Popped = -1
    return Popped

for i in range(11):
    Data = int(input("Please input a number:"))
    result = Push(Data)
    if result == True:
        print("Success")
    else:
        print("Stack is full.")

for i in range(10):
    print(StackData[i], end = " ")

print()

Pop()
Pop()
for i in range(10):
    print(StackData[i], end = " ")