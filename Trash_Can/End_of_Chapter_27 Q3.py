# (a) QueueClass contains NodeClass.

class NodeClass:
    def __init__(self):
        # 初始化节点类的私有属性
        # __data: 存储节点的数据，初始为空字符串
        # __pointer: 存储指向下一个节点的指针，初始为-1表示空指针
        self.__data = ""            #Private attribute, type: STRING
        self.__pointer = -1        #Private attribute, type: INTEGER
    
    def SetData(self, d):
        # 设置节点的数据字段
        # 参数: d - 要存储在节点中的数据（字符串类型）
        self.__data = d
    
    def GetData(self):
        # 获取节点中存储的数据
        # 返回: 节点中存储的字符串数据
        return self.__data

    def SetPointer(self, x):
        # 设置节点的指针字段
        # 参数: x - 指向下一个节点的索引值（整数类型）
        self.__pointer = x
    
    def GetPointer(self):
        # 获取节点的指针值
        # 返回: 指向下一个节点的索引值（整数类型）
        return self.__pointer
    
class QueueClass:
    def __init__(self):
        # 初始化队列类的私有属性
        # __Queue: 存储NodeClass对象的列表，容量范围为0到50
        # __head: 队列头部指针，初始为-1表示队列为空
        # __tail: 队列尾部指针，初始为-1表示队列为空
        self.__Queue = []               #Private attribute, type: List of NodeClass, range: 0 to 50
        self.__head = -1                #Private attribute, type: INTEGER
        self.__tail = -1                #Private attribute, type: INTEGER
    
    def JoinQueue(self, d):
        # 将新元素加入队列的方法
        # 参数: d - 要加入队列的数据
        # 创建一个新的NodeClass实例，设置其数据，然后添加到队列列表中
        Node = NodeClass()
        Node.SetData(d)
        self.__Queue.append(Node)

# 主程序测试
# 创建一个队列实例
queue = QueueClass()

# 测试添加元素到队列
print("测试 JoinQueue 方法:")
queue.JoinQueue("First")
queue.JoinQueue("Second")
queue.JoinQueue("Third")

# 检查队列中的元素
print("队列中的元素数量:", len(queue._QueueClass__Queue))

# 访问队列中的节点数据（通过私有属性访问）
for i in range(len(queue._QueueClass__Queue)):
    node = queue._QueueClass__Queue[i]
    print(f"节点 {i} 的数据: {node.GetData()}")

# 创建一个节点实例进行测试
print("\n测试 NodeClass:")
node1 = NodeClass()
node1.SetData("Test Data")
node1.SetPointer(5)

print(f"节点数据: {node1.GetData()}")
print(f"节点指针: {node1.GetPointer()}")

# 测试修改数据和指针
node1.SetData("New Test Data")
node1.SetPointer(10)

print(f"修改后的节点数据: {node1.GetData()}")
print(f"修改后的节点指针: {node1.GetPointer()}")

# 验证队列的初始状态
print(f"\n队列头指针: {queue._QueueClass__head}")
print(f"队列尾指针: {queue._QueueClass__tail}")
