# 定义一个名为 Car 的类，用于表示汽车对象
class Car:
    # 构造函数（初始化方法），在创建新对象时自动调用
    def __init__(self, n, e):
        # 私有属性，存储车辆的唯一标识符
        self.__VehicleID = n              #Private attribute, Type: STRING
        # 私有属性，存储车辆的注册号码，初始为空字符串
        self.__Registration = ""          #Private attribute, Type: STRING
        # 私有属性，存储车辆的注册日期，初始为 None（无值）
        self.__DateOfRegistration = None  #Private attribute, Type: DATE
        # 私有属性，存储发动机排量，接收构造函数传入的参数 e
        self.__EngineSize = e             #Private attribute, Type: INTEGER
        # 私有属性，存储购买价格，初始为 0.00
        self.__PurchasePrice = 0.00       #Private attribute, Type: REAL

    # 使用 @property 装饰器定义 PurchasePrice 的 getter 方法
    # 允许通过 MyCar.PurchasePrice 访问私有属性 __PurchasePrice
    @property
    def PurchasePrice(self):
        return self.__PurchasePrice

    # 使用 @PurchasePrice.setter 装饰器定义 PurchasePrice 的 setter 方法
    # 允许通过 MyCar.PurchasePrice = value 设置私有属性 __PurchasePrice
    @PurchasePrice.setter
    def PurchasePrice(self, p):
        self.__PurchasePrice = p

    # 使用 @property 装饰器定义 DateOfRegistration 的 getter 方法
    # 允许通过 MyCar.DateOfRegistration 访问私有属性 __DateOfRegistration
    @property
    def DateOfRegistration(self):
        return self.__DateOfRegistration

    # 使用 @DateOfRegistration.setter 装饰器定义 DateOfRegistration 的 setter 方法
    # 允许通过 MyCar.DateOfRegistration = date_value 设置私有属性 __DateOfRegistration
    @DateOfRegistration.setter
    def DateOfRegistration(self, d):
        self.__DateOfRegistration = d

    # 使用 @property 装饰器定义 Registration 的 getter 方法
    # 允许通过 MyCar.Registration 访问私有属性 __Registration
    @property
    def Registration(self):
        return self.__Registration	

    # 使用 @Registration.setter 装饰器定义 Registration 的 setter 方法
    # 允许通过 MyCar.Registration = reg_value 设置私有属性 __Registration
    @Registration.setter
    def Registration(self, r):
        self.__Registration = r

    # 使用 @property 装饰器定义 VehicleID 的 getter 方法
    # 因为 VehicleID 只需要读取，所以只定义了 getter，没有 setter
    # 这使得 __VehicleID 成为只读属性
    @property
    def VehicleID(self):
        return self.__VehicleID

    # 使用 @property 装饰器定义 EngineSize 的 getter 方法
    # 因为 EngineSize 只需要读取，所以只定义了 getter，没有 setter
    # 这使得 __EngineSize 成为只读属性
    @property
    def EngineSize(self):
        return self.__EngineSize

# 创建一个新的 Car 类实例 (对象)，将它赋值给变量 MyCar
# 调用构造函数 __init__，传递 "abc1234" 作为 VehicleID，2500 作为 EngineSize
MyCar=Car("abc1234", 2500)

# 使用之前定义的 setter 方法，设置购买价格为 100000
MyCar.PurchasePrice = 100000

# 使用之前定义的 setter 方法，设置注册日期为 "27-11-2025"
MyCar.DateOfRegistration = "27-11-2025"

# 使用之前定义的 setter 方法，设置注册号码为 "BMW740"
MyCar.Registration = "BMW740"

# 使用之前定义的 getter 方法，打印当前的购买价格
print(MyCar.PurchasePrice)
# 使用之前定义的 getter 方法，打印当前的注册日期
print(MyCar.DateOfRegistration)
# 使用之前定义的 getter 方法，打印当前的注册号码
print(MyCar.Registration)
# 使用之前定义的 getter 方法，打印发动机排量
print(MyCar.EngineSize)
# 使用之前定义的 getter 方法，打印车辆 ID
print(MyCar.VehicleID)