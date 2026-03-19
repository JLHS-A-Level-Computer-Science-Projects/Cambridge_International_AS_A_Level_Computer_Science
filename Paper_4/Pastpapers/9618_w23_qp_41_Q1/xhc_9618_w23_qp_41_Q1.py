#Created by xhc2008

def IterativeVowels(Value) -> int:
    #Declare Total as Integer
    #Declare LengthString as Integer
    #Declare FirstCharacter as Char
    Total=0
    LengthString=len(Value)
    for x in range(0,LengthString):
        FirstCharacter=Value[0:1]
        if FirstCharacter in ['a','e','i','o','u']:
            Total=Total+1
        Value=Value[1:len(Value)]
    return Total

def RecursiveVowels(Value) -> int:
    return int(Value[0] in ['a','e','i','o','u']) + RecursiveVowels(Value[1:]) if Value else 0

def r(v) -> int:
    return int(v[0] in ['a','e','i','o','u']) + r(v[1:]) if v else 0


print(IterativeVowels("house"))
print(RecursiveVowels("house"))