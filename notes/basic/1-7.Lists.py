# --- List 概念 ---
# List 是可變動 (mutable) 的有序的、可變更的，可存放不同型別元素。
phreas = ["melo",2, "顆", True]
print(phreas)
print(type(phreas))  #檢視資料型態

fruits = ["apple", "banana", "cherry"]
print(fruits)

# --- 透過索引存取元素 ---
print(fruits[0])   # apple
print(fruits[-1])  # cherry

# --- 切片 (Slicing) ---
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']

# --- 修改元素 (List 是可變動的) ---
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# --- 新增元素 ---
fruits.append("mango")       # 加到最後
fruits.insert(1, "kiwi")     # 插入到指定位置
fruits.extend(phreas)        # 在列表後延伸加入另一個物件，如：lists, tuples, sets, dictionaries
print(fruits)

# --- 刪除元素 ---
fruits.remove("apple")   # 移除指定值 (若不存在會報錯)
fruits.pop(2)            # 移除指定索引 (未輸入情況下則移除最後一個)
del fruits[0]            # 用 del 刪除某一項
print(fruits)

# --- 清空 / 刪除整個 List ---
temp = [1,2,3]
temp.clear()  # 清空列表
print(temp)

# del temp  # 完全刪除這個變數本身
del temp

# --- List 長度 ---
print(len(fruits))

# --- List Loop (迴圈) ---
for item in fruits:
    print(item)

# --- 判斷元素是否存在 (成員運算子) ---
print("mango" in fruits)

# --- List 合併 ---
list1 = [1,2,3]
list2 = [4,5,6]
merged = list1 + list2    # 方法1
print(merged)

list1.extend(list2)       # 方法2
print(list1)

for x in list2:           # 方法3
    list1.append(x)
print(list1)

# --- List 複製 ---
fruits = ["apple", "banana", "cherry"]
copy_list1 = fruits.copy()  # 方法1
copy_list2 = list(fruits)   # 方法2
copy_list3 = fruits[:]      # 方法3
print(copy_list3)

# --- 排序與反轉 ---
numbers = [3, 1, 5, 2, 4]
numbers.sort()   # 正向排序
print(numbers)

numbers.sort(reverse=True)  # 反向排序
print(numbers)

numbers.reverse()  # 反轉元素順序
print(numbers)

# --- List Comprehension (列表生成式) ---
# 用簡潔方式建立新列表

nums = [1,2,3,4,5]
squares = [n*n for n in nums]
print(squares)

# 帶條件的 List Comprehension
odds = [n for n in nums if n % 2 == 1]
print(odds)

# --- 巢狀 List (Nested List) ---
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])  # 6

# --- 小結 ---
# ✅ List 是可變動、有序的序列
# ✅ 使用索引與切片存取元素
# ✅ append() / insert() / remove() / pop() 進行修改
# ✅ sort()、reverse()、copy()、clear() 常用方法
# ✅ 可用 List Comprehension 建立新列表
