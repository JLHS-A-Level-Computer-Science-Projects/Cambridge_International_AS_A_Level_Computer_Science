# =============================
# Python 文件操作教学示例
# =============================

# 1️⃣ 写入文件（覆盖模式）
print("1. 写入文件（覆盖模式）")
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 世界！\n")
    file.write("这是第一行。\n")
    file.write("这是第二行。\n")

print("✅ 文件写入完成（覆盖模式）\n")

# 2️⃣ 读取整个文件内容
print("2. 读取整个文件内容")
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("文件内容：")
    print(content)

print("✅ 文件读取完成\n")

# 3️⃣ 逐行读取文件
print("3. 逐行读取文件")
with open("example.txt", "r", encoding="utf-8") as file:
    print("逐行输出：")
    for line in file:
        print(f"-> {line.strip()}")  # .strip() 去除换行符

print("✅ 逐行读取完成\n")

# 4️⃣ 追加内容到文件末尾
print("4. 追加内容到文件")
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("这是追加的第三行。\n")
    file.write("这是追加的第四行。\n")

print("✅ 内容追加完成\n")

# 5️⃣ 再次读取确认追加内容
print("5. 重新读取文件确认追加内容")
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # 读取所有行到列表
    for i, line in enumerate(lines, 1):
        print(f"第{i}行: {line.strip()}")

print("✅ 最终内容确认完成\n")

# 6️⃣ 检查文件是否存在（可选进阶）
import os

print("6. 检查文件是否存在")
if os.path.exists("example.txt"):
    print("✅ 文件 example.txt 存在")
else:
    print("❌ 文件不存在")

# 7️⃣ 删除文件（谨慎使用，教学演示）
print("\n7. 删除文件（教学演示）")
try:
    os.remove("example.txt")
    print("✅ 文件已删除")
except FileNotFoundError:
    print("❌ 文件不存在，无法删除")