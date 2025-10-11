# 定义常量
EMPTY_STR = ""  # 空字符串常量，用于表示空值
NULL_PTR = -1   # 空指针常量，表示无效的指针位置
MAX_QUEUE_SIZE = 8  # 队列的最大容量

# 初始化队列，使用列表存储队列元素
queue = ["" for i in range(0, MAX_QUEUE_SIZE)]

def initialiseQueue() -> None:
    """初始化队列
    设置队列的前端指针和成员计数器为初始状态
    """
    global frontQueuePtr, queueMemberCnt
    frontQueuePtr = 0  # 队列前端指针，指向下一个要出队的元素
    queueMemberCnt = 0  # 队列中当前元素的数量

def addToQueue(newItem) -> None:
    """向队列添加新元素（入队操作）
    
    参数:
        newItem: 要添加到队列的新元素
        
    异常:
        Exception: 当队列已满时抛出
    """
    global frontQueuePtr, queueMemberCnt, queue, EMPTY_STR, NULL_PTR, MAX_QUEUE_SIZE
    # 检查队列是否已满
    if queueMemberCnt >= MAX_QUEUE_SIZE:
        raise Exception("Queue is full")
    
    # 计算队列尾端指针位置（使用模运算实现循环队列）
    endQueuePtr = (frontQueuePtr + queueMemberCnt) % MAX_QUEUE_SIZE
    # 在尾端位置添加新元素
    queue[endQueuePtr] = newItem
    # 增加队列成员计数
    queueMemberCnt += 1

def removeFromQueue() -> str:
    """从队列移除元素（出队操作）
    
    返回:
        str: 从队列前端移除的元素
        
    异常:
        Exception: 当队列为空时抛出
    """
    global frontQueuePtr, queueMemberCnt, queue, EMPTY_STR, NULL_PTR, MAX_QUEUE_SIZE
    # 检查队列是否为空
    if queueMemberCnt == 0:
        raise Exception("Queue is empty!")
    
    # 获取前端指针位置的元素
    item = queue[frontQueuePtr]
    # 减少队列成员计数
    queueMemberCnt -= 1
    # 移动前端指针到下一个位置（使用模运算实现循环队列）
    frontQueuePtr += 1
    frontQueuePtr %= MAX_QUEUE_SIZE
    # 返回出队的元素
    return item