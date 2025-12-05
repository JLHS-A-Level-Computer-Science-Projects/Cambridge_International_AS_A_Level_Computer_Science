# 定义哈希函数，使用除法取余法，将键值映射到 0-9 的索引范围内
def HashFunc(Key):
	return Key % 10

# 定义哈希表的最大容量为 10
MaxSizeTable = 10
# 初始化哈希表，创建一个包含 10 个元素的列表，所有元素初始值为 -1，表示该位置为空
HashTable = [-1 for i in range(MaxSizeTable)]

# 向哈希表中插入新记录的函数
def Insert(NewRecord):
	# 用于计数，记录哈希表中已插入的元素数量（在当前实现中未被有效利用）
	NumberInTable = 0
	# 计算新记录应插入的初始索引位置
	Index = HashFunc(NewRecord)
	# 当目标索引位置已被占用（不等于 -1）时，执行循环查找下一个可用位置
	while HashTable[Index] != -1:
		# 索引向后移动一位
		Index += 1
		# 更新计数器
		NumberInTable += 1
		# 如果索引超出表的最大范围（即大于 9），则将其重置为 0，实现循环查找（开放寻址法中的线性探测）
		if Index > MaxSizeTable:
			Index = 0
	# 找到空位置后，将新记录插入到该位置
	HashTable[Index] = NewRecord

# 在哈希表中查找指定记录的函数
def FindRecord(SearchKey):
	# 计算搜索键值的初始哈希索引
	Index = HashFunc(SearchKey)
	# 当前索引位置的值既不等于要查找的键值，也不是空位（-1）时，继续循环查找
	# 这意味着当前位置可能是因为冲突而被其他键值占用的
	while HashTable[Index] != SearchKey and HashTable[Index] != -1:
		# 索引向后移动一位
		Index += 1
		# 如果索引超出表的最大范围，则将其重置为 0，实现循环查找
		if Index > MaxSizeTable:
			Index = 0
	# 循环结束后，如果当前位置不是空位（-1），则说明找到了要查找的记录
	if HashTable[Index] != -1:
		# 返回找到的记录值
		return HashTable[Index]
	# 如果当前位置是 -1，表示查找失败，该键值不存在于表中，函数会默认返回 None