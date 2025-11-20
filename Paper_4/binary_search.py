import random

list1 = [0 for i in range(10)] #初始化list1，包含10个整数类型的元素
NumberToBeSearched = random.randint(1,100) #搜索1到100之间的随机数

#美化输出
print()
print("NumberToBeSearched:",NumberToBeSearched)
print()

#赋值list1
for i in range(10):
	list1[i] = random.randint(1,100) 

def __insertion_sort__():
	for i in range(1,len(list1)):
		ItemToBeInserted = list1[i]
		CurrentItem = i - 1
		while list1[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
			list1[CurrentItem + 1] = list1[CurrentItem]
			CurrentItem -= 1
		list1[CurrentItem + 1] = ItemToBeInserted
	print(list1)

def __binary_search__(ListToBeSearchedFrom):
	SearchFailed = False
	FirstIndex = 0
	LastIndex = len(ListToBeSearchedFrom) - 1
	while True:
		Middle = (FirstIndex + LastIndex) // 2
		if ListToBeSearchedFrom[Middle] == NumberToBeSearched:
			print("Element found at:", Middle)
			break
		else:
			if FirstIndex >= LastIndex:
				print("404 Not Found")
				break
			else:
				if ListToBeSearchedFrom[Middle] > NumberToBeSearched:
					LastIndex = Middle - 1
				else:
					FirstIndex = Middle + 1

try:
	__insertion_sort__()
	__binary_search__(list1)
except Exception as e:
	print("Exceptions:",e)
finally:
	pass