# 定义常量
EMPTY_STR = ""  # 空字符串常量，用于表示空值
NULL_PTR = -1   # 空指针常量，表示无效的指针位置
MAX_STACKSIZE = 8  # 栈的最大容量

# 初始化栈指针和栈数组
baseOfStackPtr = NULL_PTR  # 栈底指针
topOfStackPtr = NULL_PTR   # 栈顶指针
stack = [EMPTY_STR for i in range(0, MAX_STACKSIZE)]  # 栈数组

def initialiseStack() -> None:
    """初始化栈
    设置栈的底指针和顶指针为初始状态
    """
    global baseOfStackPtr, topOfStackPtr
    baseOfStackPtr = 0      # 栈底指针指向数组起始位置
    topOfStackPtr = NULL_PTR  # 栈顶指针初始化为空，表示栈为空

def push(newItem: str) -> None:
    """向栈压入新元素（入栈操作）
    
    参数:
        newItem (str): 要压入栈的新元素
        
    异常:
        Exception: 当栈已满时抛出
    """
    global topOfStackPtr, stack, MAX_STACKSIZE
    # 检查栈是否已满
    if topOfStackPtr >= MAX_STACKSIZE - 1:
        raise Exception("Stack is full!")
    
    # 栈顶指针上移
    topOfStackPtr = topOfStackPtr + 1
    # 在栈顶位置存入新元素
    stack[topOfStackPtr] = newItem

def pop() -> str:
    """从栈弹出元素（出栈操作）
    
    返回:
        str: 从栈顶弹出的元素
        
    异常:
        Exception: 当栈为空时抛出
    """
    global topOfStackPtr, stack
    # 检查栈是否为空
    if topOfStackPtr == NULL_PTR:
        raise Exception("Stack is empty!")
    
    # 获取栈顶指针位置的元素
    item = stack[topOfStackPtr]
    # 栈顶指针下移
    topOfStackPtr -= 1
    # 返回弹出的元素
    return item