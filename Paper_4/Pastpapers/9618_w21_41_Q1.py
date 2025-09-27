def Unknown(x,y):
	if x < y:
		print(x + y)
		return (Unknown(x + 1,y) * 2)
	else:
		if x == y:
			return 1
		else:
			print(x + y)
			return (Unknown(x - 1,y) // 2)
'''
print(10,15)
print("return:",Unknown(10,15))
print()
print(10,10)
print("return:",Unknown(10,10))
print()
print(15,10)
print("return:",Unknown(15,10))
'''

def IterativeUnknown(x,y):
	answer = 1
	while x != y:
		print(x + y)
		if x < y:
			x += 1
			answer *= 2
		if x > y:
			x -= 1
			answer //= 2
	return answer

print(10,15)
print("return:",IterativeUnknown(10,15))
print()
print(10,10)
print("return:",IterativeUnknown(10,10))
print()
print(15,10)
print("return:",IterativeUnknown(15,10))