Vowels = ['a','e','i','o','u']
def RecursiveVowels(InString):
	Total = 0
	if len(InString) == 0:
		return Total
	if InString[0] in Vowels:
		Total += 1
		return 1 + RecursiveVowels(InString[1:len(InString)])
	else:
		return RecursiveVowels(InString[1:len(InString)])

print(RecursiveVowels("imagine"))