class Person:
    def __init__(self, n, a):
        """
        构造函数/初始化方法
        当创建Person对象时会自动调用此方法
        参数:
        self: 反正就是必须写
        n: 姓名 - 字符串类型
        a: 年龄 - 整数类型
        """
        # 在Python中，属性名前加双下划线(__)表示私有属性（Private）
        # 私有属性只能在类的内部访问，外部不能直接访问
        #使用python需要使用注释写明“private”和数据类型
        self.__name = n #Private attribute, Type: STRING
        self.__age = a #Private attribute, Type: INTEGER
        self.__height = 0 #Private attribute, Type: REAL
        self.__weight = 0 #Private attribute, Type: REAL

    def SetHeight(self, h):
        """
        设置身高
        用于设置/修改身高属性
        """
        self.__height = h

    def SetWeight(self, w):
        """
        设置体重方法
        用于设置/修改体重属性
        """
        self.__weight = w

    def GetName(self):
        """
        获取姓名方法
        返回私有属性__name的值
        """
        return self.__name

    def GetAge(self):
        """
        获取年龄方法
        返回私有属性__age的值
        """
        return self.__age

    def BMI(self):
        """
        计算身体质量指数(BMI)
        BMI = 体重(kg) / 身高(m)²
        """
        # 使用体重除以身高的平方来计算BMI
        return (self.__weight / (self.__height ** 2))# **在python中表示乘方


# ====================== 使用Person类 ======================

# 创建Person类的实例/对象
# 调用构造函数__init__，传入姓名"A"和年龄17
NewPerson = Person("A", 17)

# 使用设置方法设置身高（单位：米）
NewPerson.SetHeight(1.8)

# 使用设置方法设置体重（单位：千克）
NewPerson.SetWeight(72)

# 输出个人信息
# 使用获取方法获取姓名并打印
print(NewPerson.GetName())    # 输出: A

# 使用获取方法获取年龄并打印
print(NewPerson.GetAge())     # 输出: 17

# 计算并打印BMI值
print(NewPerson.BMI())        # 输出: 22.222... (72 / 1.8² ≈ 22.22)