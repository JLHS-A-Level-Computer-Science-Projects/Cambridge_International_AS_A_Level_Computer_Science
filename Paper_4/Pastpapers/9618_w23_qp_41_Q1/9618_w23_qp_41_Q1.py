#Created by 4AMAlan

def IterativeVowel(Value) -> int:
    Total = 0
    LengthString = len(Value)
    for i in range(LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1:LengthString]
    return Total

def RecursiveVowel(Value):
    if len(Value) == 0:
        return 0
    else:
        if Value[0] == 'a' or Value[0] == 'e' or Value[0] == 'i' or Value[0] == 'o' or Value[0] == 'u':
            return 1 + RecursiveVowel(Value[1:])
        else:
            return RecursiveVowel(Value[1:])

print(IterativeVowel("house"))
print(RecursiveVowel('imagine'))