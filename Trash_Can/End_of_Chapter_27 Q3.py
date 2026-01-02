# (a) QueueClass contains NodeClass.

class NodeClass:
    def __init__(self):
        self.__data = ""            #Private attribute, type: STRING
        self.__pointer = -1         #Private attribute, type: INTEGER
    
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
        self.__Queue = []               #Private attribute, type: List of NodeClass, range: 0 to 50
        self.__head = -1                #Private attribute, type: INTEGER
        self.__tail = -1                #Private attribute, type: INTEGER
    
    def JoinQueue(self, d):
        Node = NodeClass()
        Node.SetData(d)
        self.__Queue.append(Node)

