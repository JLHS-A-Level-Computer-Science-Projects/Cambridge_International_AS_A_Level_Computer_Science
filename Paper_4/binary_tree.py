#Annotated by Qwen3-Coder
# 定义空指针的值，表示没有指向任何节点
NULLPOINTER = -1

class treenode:          # 建立节点类对象
    def __init__(self):
        self.data = ""        # 存储节点数据
        self.left = 0         # 左子节点的索引指针
        self.right = 0        # 右子节点的索引指针

# 创建一个包含7个treenode对象的列表，模拟静态数组
thistree = [treenode() for i in range(0, 7)]

# 全局变量：根节点指针和空闲节点指针
rootpointer = 0    # 指向二叉搜索树的根节点
FreePtr = 0        # 指向空闲链表的头部

def initialise():
    """
    初始化二叉搜索树：
    - 设置根节点指针为空
    - 设置空闲指针指向索引0
    - 初始化空闲链表（将所有节点链接起来）
    - 清空所有节点的数据
    """
    global rootpointer, FreePtr
    
    # 初始化根节点指针为空（表示树为空）
    rootpointer = NULLPOINTER
    
    # 初始化空闲指针，指向第一个可用节点（索引0）
    FreePtr = 0
    
    # 初始化空闲链表：将所有节点通过left指针连接起来
    # 这样可以快速找到下一个可用的节点位置
    for index in range(6):  # 索引0到5
        thistree[index].left = index + 1  # 每个节点的left指针指向下个节点
        thistree[index].right = NULLPOINTER  # right指针设为空（因为这是空闲链表）
    
    # 最后一个节点（索引6）的左右指针都设为空
    thistree[6].left = thistree[6].right = NULLPOINTER
    
    # 清空所有节点的数据字段
    for index in range(7):
        thistree[index].data = 'empty'

def outputtree():   
    """
    输出整个树的结构信息：
    - 显示根节点指针和空闲指针的当前值
    - 显示每个节点的索引、左指针、数据和右指针
    """
    global rootpointer, FreePtr
    
    # 输出根节点指针和空闲指针的状态
    print("start:", rootpointer, "free:", FreePtr)
    
    # 遍历并输出每个节点的信息
    for i in range(7):
        print('[', i, ']', end="  ")  # 输出节点索引
        print(thistree[i].left, end="  ")     # 输出左指针
        print(thistree[i].data, end="  ")     # 输出节点数据
        print(thistree[i].right)              # 输出右指针

def traveltree(TreeNodePointer):
    """
    中序遍历二叉搜索树（递归实现）
    遍历顺序：左子树 -> 根节点 -> 右子树
    这样可以按升序输出所有节点的数据
    """
    # 递归终止条件：如果节点指针为空，直接返回
    if TreeNodePointer == NULLPOINTER:
        return
    
    # 递归遍历左子树
    traveltree(thistree[TreeNodePointer].left)
    
    # 访问当前节点（输出数据）
    print(thistree[TreeNodePointer].data)
    
    # 递归遍历右子树
    traveltree(thistree[TreeNodePointer].right)

def insertnode(newitem):
    """
    向二叉搜索树中插入新节点
    参数：newitem - 要插入的数据
    """
    global rootpointer, FreePtr
    
    # 检查是否有空闲节点可用
    if FreePtr != NULLPOINTER:
        # 获取一个空闲节点的位置
        newnodeptr = FreePtr           # 新节点的索引位置
        FreePtr = thistree[FreePtr].left  # 更新空闲指针，指向下个空闲节点
        
        # 设置新节点的数据和指针
        thistree[newnodeptr].data = newitem      # 存储数据
        thistree[newnodeptr].left = NULLPOINTER  # 左指针初始化为空
        thistree[newnodeptr].right = NULLPOINTER # 右指针初始化为空
        
        # 如果树为空（根节点指针为空），新节点成为根节点
        if rootpointer == NULLPOINTER:
            rootpointer = newnodeptr
        else:
            # 树不为空，需要找到新节点的正确插入位置
            thisnodeptr = rootpointer  # 从根节点开始搜索
            
            # 循环查找插入位置
            while thisnodeptr != NULLPOINTER:
                previousnodeptr = thisnodeptr  # 记录当前节点作为父节点
                
                # 根据数据大小决定向左还是向右搜索
                if thistree[thisnodeptr].data > newitem:
                    # 新数据小于当前节点数据，向左子树搜索
                    tureleft = True  # 标记应该插入到左子树
                    thisnodeptr = thistree[thisnodeptr].left
                else:   
                    # 新数据大于等于当前节点数据，向右子树搜索
                    tureleft = False  # 标记应该插入到右子树
                    thisnodeptr = thistree[thisnodeptr].right
            
            # 将新节点连接到父节点的相应位置
            if tureleft == True:
                # 插入到父节点的左子树
                thistree[previousnodeptr].left = newnodeptr
            else:
                # 插入到父节点的右子树
                thistree[previousnodeptr].right = newnodeptr

# 程序执行部分
# 1. 初始化树结构
initialise()

# 2. 输出初始化后的树状态
outputtree()

# 3. 插入节点 A, B, C, D
insertnode('A')
insertnode('B') 
insertnode('C')
insertnode('D')

# 4. 输出插入节点后的树状态
outputtree()

# 5. 中序遍历输出树中的所有数据（按升序排列）
traveltree(rootpointer)
