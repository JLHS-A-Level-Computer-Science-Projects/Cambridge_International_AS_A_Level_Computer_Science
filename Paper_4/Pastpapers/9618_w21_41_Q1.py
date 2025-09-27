#Created by 4AMAlan

def Unknown(x, y):
    """
    递归函数：根据x和y的关系进行不同的递归操作
    
    递归逻辑：
    - 当 x < y：打印(x+y)，然后返回 2 * Unknown(x+1, y)
    - 当 x == y：返回 1（递归终止条件）
    - 当 x > y：打印(x+y)，然后返回 Unknown(x-1, y) // 2
    
    这个函数实际上计算的是：从x到y的路径上，每次移动都进行乘2或除2操作
    """
    if x < y:
        print(x + y)  # 打印当前x和y的和
        return (Unknown(x + 1, y) * 2)  # 递归：x向y靠近，结果乘2
    else:
        if x == y:
            return 1  # 基准情形：x等于y时返回1（递归终止）
        else:
            print(x + y)  # 打印当前x和y的和
            return (Unknown(x - 1, y) // 2)  # 递归：x向y靠近，结果除2

# 测试递归版本
print(10,15)
print("return:",Unknown(10,15))
print()
print(10,10)
print("return:",Unknown(10,10))
print()
print(15,10)
print("return:",Unknown(15,10))

def IterativeUnknown(x, y):
    """
    迭代版本：使用循环实现与递归函数相同的功能
    
    实现思路：
    1. 初始化答案为1（对应递归中的基准情形）
    2. 当x不等于y时循环：
       - 打印x+y
       - 如果x < y：x增加，答案乘2（模拟递归的乘2操作）
       - 如果x > y：x减少，答案除2（模拟递归的除2操作）
    3. 当x等于y时返回答案
    
    这种方法避免了递归的函数调用开销，更高效。
    """
    answer = 1  # 对应递归中x==y时返回1的情况
    while x != y:
        print(x + y)
        if x < y:
            x += 1      # x向y靠近（增加）
            answer *= 2  # 对应递归中的乘2操作
        if x > y:       # 这里用if而不是elif，确保逻辑清晰
            x -= 1      # x向y靠近（减少）
            answer //= 2  # 对应递归中的整除2操作
    return answer

# 测试迭代版本
print(10,15)
print("return:",IterativeUnknown(10,15))
print()
print(10,10)
print("return:",IterativeUnknown(10,10))
print()
print(15,10)

print("return:",IterativeUnknown(15,10))
