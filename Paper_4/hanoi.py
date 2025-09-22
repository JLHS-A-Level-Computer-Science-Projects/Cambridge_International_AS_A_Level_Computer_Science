#Created by 4AMAlan

def hanoi(n,a,b,c): #n为初始盘子个数（整数类型），a为初始柱（字符串类型），b为中转柱（字符串类型），c为目标柱（字符串类型）
    if n == 1:
        print("将盘子从",a,"移动到",c)
    else:
       hanoi(n-1, a, c, b)
       print("将盘子从",a,"移动到",c)
       hanoi(n-1, b, a, c)

n = int(input("请输入递归层数:"))
hanoi(n, 'a', 'b', 'c')