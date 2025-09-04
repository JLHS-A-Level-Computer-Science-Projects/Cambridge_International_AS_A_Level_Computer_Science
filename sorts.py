#Produced by 4AMAlan
import random

list1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def rand():
	for i in range(0,len(list1)):
		list1[i] = random.randint(1,100)

def bubblesort():
    for i in range(len(list1)-1,0,-1):
        for j in range(0,i):
            if list1[j] > list1[j + 1]:
                list1[j],list1[j + 1] = list1[j + 1],list1[j]
    print(list1)

def improvedbubblesort():
	NoMoreSwaps = False
	while not NoMoreSwaps:
		NoMoreSwaps = True
		for j in range(0,len(list1)-1):
			if list1[j] > list1[j + 1]:
				list1[j],list1[j + 1] = list1[j + 1],list1[j]
				NoMoreSwaps = False
	print(list1)

def insertionsort():
	for i in range(0,len(list1)):
		ItemToBeInsterted = list1[i]
		CurrentItem = i - 1
		while list1[CurrentItem] > ItemToBeInsterted and CurrentItem > -1:
			list1[CurrentItem + 1] = list1[CurrentItem]
			CurrentItem = CurrentItem - 1
		list1[CurrentItem + 1] = ItemToBeInsterted
	print(list1)

rand()
print(list1)

improvedbubblesort()
