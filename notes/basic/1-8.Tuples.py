# --- Tuple 概念 ---
# Tuple 與 List 類似，都是有序序列，但「不可變」（immutable）
# 代表：建立後不能修改、加入、刪除元素

fruits = ("apple", "banana", "cherry")
print(fruits)

# --- 單一元素 Tuple ---
# 若要建立只有一個元素的 Tuple，需要在後面加逗號
single = ("apple",)
print(type(single))

# 沒加逗號就會變成字串
not_tuple = ("apple")
print(type(not_tuple))

# --- 透過索引存取元素 ---
print(fruits[0])  # apple
print(fruits[-1]) # cherry

# --- 切片 (Slicing) ---
print(fruits[0:2])  # ('apple', 'banana')
print(fruits[:2])   # ('apple', 'banana')
print(fruits[1:])   # ('banana', 'cherry')

# --- Tuple 是不可變的 (不能直接修改) ---
# fruits[1] = "kiwi"  # 會報錯！！

# 若要修改，只能先轉成 list，再轉回 tuple

fruits_list = list(fruits)
fruits_list[1] = "kiwi"
fruits = tuple(fruits_list)
print(fruits)

# --- Tuple 合併 ---
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

# --- 重複 Tuple ---
t4 = ("Hi",) * 3
print(t4)

# --- 判斷元素是否存在 ---
print("apple" in fruits)

# --- Tuple 長度 ---
print(len(fruits))

# --- Tuple 迴圈 ---
for item in fruits:
    print(item)

# --- Unpacking (拆解 Tuple) ---
tuple_data = ("承諺", 24, "Data Engineer")
name, age, job = tuple_data
print(name, age, job)

# 若元素數量不一致，可以使用 * 收集剩餘項目
numbers = (1, 2, 3, 4, 5)
a, b, *others = numbers
print(a, b, others)  # others -> [3, 4, 5]

# --- Tuple 的使用情境 ---
# ✅ 用在不希望被修改的資料
# ✅ 可以作為字典的 key (因為 tuple 是可 hash)
# ✅ 多變數同時回傳或接收

# --- 小結 ---
# ✅ Tuple：有序、不可變、可包含不同型別
# ✅ 單一元素記得加逗號 → ("apple",)
# ✅ 不能直接修改，需轉 list 再轉回
# ✅ 支援合併、切片、成員判斷、迴圈
# ✅ 可進行 Unpacking，非常適合多值回傳

# 建議練習：
# 1. 將你的基本資料存為 tuple，並用 unpacking 輸出格式化介紹文字。
# 2. 嘗試撰寫一個函式同時回傳多個值，並用 tuple 接收。
# 3. 練習辨識哪些資料應該用 list？哪些應該用 tuple？
