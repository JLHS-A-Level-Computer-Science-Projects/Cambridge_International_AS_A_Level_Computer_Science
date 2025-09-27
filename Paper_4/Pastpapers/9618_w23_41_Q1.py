#Created by 4AMAlan

# 定义元音字母列表（注意：这里只包含小写元音）
Vowels = ['a','e','i','o','u']

def RecursiveVowels(InString):
    """
    使用递归方法计算字符串中元音字母的数量
    
    递归思想：将大问题分解为小问题
    - 基本情况：空字符串，元音数量为0
    - 递归步骤：检查第一个字符 + 剩余字符串的元音数量
    
    参数:
        InString: 要检查的字符串
        
    返回:
        字符串中元音字母的总数
    """
    
    Total = 0  # 当前递归层级的计数器
    
    # 基本情况：如果字符串为空，返回0（递归的终止条件）
    # 这是递归的"出口"
    if len(InString) == 0:
        return Total
    
    # 递归步骤：检查当前字符串的第一个字符
    if InString[0] in Vowels:
        # 如果第一个字符是元音
        Total += 1  # 当前层级计数加1
        # 关键递归调用：1（当前元音） + 剩余字符串的元音数量
        # 当前问题 = 当前字符的问题 + 子字符串的问题
        return 1 + RecursiveVowels(InString[1:len(InString)])
    else:
        # 如果第一个字符不是元音
        # 递归调用：只计算剩余字符串的元音数量
        return RecursiveVowels(InString[1:len(InString)])

# 测试函数

print(RecursiveVowels("imagine"))  # 输出：4（i, a, i, e）
