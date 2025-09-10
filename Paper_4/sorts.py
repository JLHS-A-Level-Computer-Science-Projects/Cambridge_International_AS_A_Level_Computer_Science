#Produced by 4AMAlan
#Annotated by DeepSeek

import random

# 初始化一个包含20个1的列表
list1 = [1 for i in range(20)]

def rand():
    """
    随机化列表函数
    将list1中的每个元素替换为1到100之间的随机整数
    """
    for i in range(0,len(list1)):
        list1[i] = random.randint(1,100)

def bubblesort():
    """
    经典冒泡排序算法
    通过多次遍历列表，比较相邻元素并交换位置，将最大元素"冒泡"到末尾
    """
    # 外层循环：从列表末尾向前遍历，每次循环减少一个需要排序的元素
    for i in range(len(list1)-1,0,-1):
        # 内层循环：遍历未排序部分，比较相邻元素
        for j in range(0,i):
            # 如果前一个元素大于后一个元素，则交换它们的位置
            if list1[j] > list1[j + 1]:
                list1[j],list1[j + 1] = list1[j + 1],list1[j]
    # 打印排序后的列表
    print(list1)

def improvedbubblesort():
    """
    改进版冒泡排序算法
    添加了提前终止机制，如果某一轮遍历中没有发生交换，说明列表已排序完成
    """
    NoMoreSwaps = False  # 标志位，用于判断是否还需要继续排序
    # 当还需要交换时继续循环
    while not NoMoreSwaps:
        NoMoreSwaps = True  # 假设本轮不需要交换（即已排序完成）
        # 遍历整个列表（除了最后一个元素）
        for j in range(0,len(list1)-1):
            # 如果前一个元素大于后一个元素
            if list1[j] > list1[j + 1]:
                # 交换元素位置
                list1[j],list1[j + 1] = list1[j + 1],list1[j]
                NoMoreSwaps = False  # 发生了交换，需要继续下一轮检查
    # 打印排序后的列表
    print(list1)

def insertionsort():
    """
    插入排序算法
    将列表分为已排序和未排序两部分，逐个将未排序元素插入到已排序部分的正确位置
    """
    # 从第二个元素开始遍历（第一个元素视为已排序）
    for i in range(0,len(list1)):
        ItemToBeInsterted = list1[i]  # 当前需要插入的元素
        CurrentItem = i - 1  # 已排序部分的最后一个元素的索引
        
        # 在已排序部分中从后向前查找插入位置
        # 当已排序元素大于待插入元素且未越界时继续向前查找
        while list1[CurrentItem] > ItemToBeInsterted and CurrentItem > -1:
            # 将较大的元素向后移动一位，为插入腾出空间
            list1[CurrentItem + 1] = list1[CurrentItem]
            CurrentItem = CurrentItem - 1  # 继续向前比较
        
        # 找到插入位置，将待插入元素放入正确位置
        list1[CurrentItem + 1] = ItemToBeInsterted
    # 打印排序后的列表
    print(list1)

# 主程序执行流程
rand()  # 首先随机化列表
print(list1)  # 打印随机化后的原始列表

improvedbubblesort()  # 执行改进版冒泡排序