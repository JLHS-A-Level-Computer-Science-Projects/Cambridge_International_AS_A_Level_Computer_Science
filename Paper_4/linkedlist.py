# 定义空指针常量，表示链表的结束
NULL_POINTER = -1

class ListNode:
    """链表节点类"""
    def __init__(self):
        # 存储节点的数据
        self.data = ""
        # 存储指向下一个节点的指针
        self.pointer = NULL_POINTER

    def __repr__(self):
        # 返回节点的字符串表示形式，格式为(数据,指针)
        return "(" + self.data + "," + str(self.pointer) + ")"

# 初始化全局变量
startPointer = NULL_POINTER  # 指向链表第一个节点的指针，初始为空
freeListPtr = NULL_POINTER   # 指向空闲节点列表第一个节点的指针，初始为空
# 创建包含6个节点的静态链表数组
LinkedList = [ListNode() for i in range(6)]

def initialiseList():
    """
    初始化链表
    将链表设置为空状态，并建立空闲节点列表
    """
    global NULL_POINTER, startPointer, freeListPtr, LinkedList
    # 将链表头指针设置为空，表示链表为空
    startPointer = NULL_POINTER
    # 将空闲列表指针指向数组的第一个位置（索引0）
    freeListPtr = 0
    # 将数组中的节点连接成一个空闲链表，形成0->1->2->3->4->5->NULL的链式结构
    for idx in range(0, 5):
        LinkedList[idx].pointer = idx + 1
    # 最后一个节点的指针设置为空，表示空闲链表的结束
    LinkedList[5].pointer = NULL_POINTER

def insertNode(newItem):
    """
    在有序链表中插入新节点
    参数: newItem - 要插入的数据项
    """
    global NULL_POINTER, startPointer, freeListPtr, LinkedList
    # 检查是否有空闲节点可用
    if freeListPtr != NULL_POINTER:
        # 获取一个空闲节点的位置
        newNodePtr = freeListPtr
        # 在该节点中存储新数据
        LinkedList[newNodePtr].data = newItem
        # 更新空闲列表指针，指向下一个空闲节点
        freeListPtr = LinkedList[freeListPtr].pointer

        # 寻找插入位置的逻辑
        # 从链表头部开始遍历
        thisNodePtr = startPointer
        # 记录前一个节点的指针
        prevNodePtr = NULL_POINTER

        # 遍历链表，寻找合适的插入位置（保持升序排列）
        while thisNodePtr != NULL_POINTER and LinkedList[thisNodePtr].data < newItem:
            prevNodePtr = thisNodePtr
            thisNodePtr = LinkedList[thisNodePtr].pointer

        # 根据插入位置进行不同的操作
        if prevNodePtr == NULL_POINTER:
            # 如果prevNodePtr仍为NULL，说明要在链表头部插入
            LinkedList[newNodePtr].pointer = startPointer  # 新节点指向原来的头节点
            startPointer = newNodePtr                      # 更新头指针指向新节点
        else:
            # 在链表中间或尾部插入
            LinkedList[newNodePtr].pointer = LinkedList[prevNodePtr].pointer  # 新节点指向原prev的下一个节点
            LinkedList[prevNodePtr].pointer = newNodePtr                     # 前一个节点指向新节点

def findNode(dataItem):
    """
    查找指定数据的节点
    参数: dataItem - 要查找的数据项
    返回: 找到的节点指针，如果未找到返回NULL_POINTER
    """
    global NULL_POINTER, startPointer, freeListPtr, LinkedList
    # 从链表头部开始查找
    thisNodePtr = startPointer
    # 遍历链表直到找到目标数据或到达链表末尾
    while thisNodePtr != NULL_POINTER and LinkedList[thisNodePtr].data != dataItem:
        thisNodePtr = LinkedList[thisNodePtr].pointer
    # 返回找到的节点指针
    return thisNodePtr

def deleteNode(dataItem):
    """
    删除指定数据的节点
    参数: dataItem - 要删除的数据项
    """
    global NULL_POINTER, startPointer, freeListPtr, LinkedList
    # 从链表头部开始查找要删除的节点
    thisNodePtr = startPointer
    # 记录前一个节点的指针
    prevNodePtr = NULL_POINTER
    # 遍历链表查找目标节点
    while thisNodePtr != NULL_POINTER and LinkedList[thisNodePtr].data != dataItem:
        prevNodePtr = thisNodePtr
        thisNodePtr = LinkedList[thisNodePtr].pointer

    # 检查是否找到要删除的节点
    if thisNodePtr == NULL_POINTER:
        # 如果未找到，抛出异常
        raise Exception("Node doesn't exist in the list.")

    # 根据要删除的节点位置进行不同的操作
    if thisNodePtr == startPointer:
        # 如果要删除的是头节点，更新头指针
        startPointer = LinkedList[startPointer].pointer
    else:
        # 如果删除的是中间或尾部节点，更新前一个节点的指针
        LinkedList[prevNodePtr].pointer = LinkedList[thisNodePtr].pointer

    # 将删除的节点重新加入空闲列表
    LinkedList[thisNodePtr].pointer = freeListPtr  # 将该节点指向当前空闲列表的头部
    freeListPtr = thisNodePtr                      # 更新空闲列表指针指向该节点

def outputAllNodes():
    """
    输出链表中所有节点的数据
    """
    global NULL_POINTER, startPointer, freeListPtr, LinkedList
    # 从链表头部开始遍历
    thisNodePtr = startPointer
    # 遍历并输出所有节点的数据
    while thisNodePtr != NULL_POINTER:
        print(LinkedList[thisNodePtr].data, end="→")  # 输出节点数据，用箭头连接
        thisNodePtr = LinkedList[thisNodePtr].pointer  # 移动到下一个节点
    print()  # 换行