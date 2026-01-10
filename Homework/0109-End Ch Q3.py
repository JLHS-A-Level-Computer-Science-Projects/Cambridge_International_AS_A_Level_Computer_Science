class NodeClass:
    def __init__(self):
        self.__data = ""            #Private, string
        self.__pointer = -1        #Private, integer
    
    def SetData(self, d):
        self.__data = d
    
    def GetData(self):
        return self.__data

    def SetPointer(self, x):
        self.__pointer = x
    
    def GetPointer(self):
        return self.__pointer
    
class QueueClass:
    def __init__(self):
        self.__Queue = []               #Private, array(0 to 50) of NodeClass
        self.__head = -1                #Private, integer
        self.__tail = -1                #Private, integer
    
    def JoinQueue(self, NewItem):
        Node = NodeClass()
        Node.SetData(NewItem)
        self.__Queue.append(Node)

    def LeaveQueue(self):
        pass
        # if self.__head == -1:
        #     return None
        # Node = self.__Queue[self.__head]
        # self.__head += 1
        # return Node.GetData()