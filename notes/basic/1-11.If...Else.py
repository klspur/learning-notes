#---If...Else---

# 基本用法
a = 1
b = 5
if b > a:
    print("b is bigger than a")

# elif 否則
# 多個條件都為 true 時，程式會執行第一個符合條件的區塊，其他的區塊則不會被執行。
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif b < a:
  print("a is greater than b")
else:
  print("a and b are equal")

# 簡短寫法
a = 5
b = 2

if a > b: print("a is greater than b")

# 內層嵌套語句：只有當外部條件為真時，內部條件才會執行
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

# 搭配 function 使用
employees = [
    {"name": "承諺", "department": "數據工程師", "salary": 50000},
    {"name": "小美", "department": "行銷", "salary": 45000},
    {"name": "阿明", "department": "業務", "salary": 48000}
]

for emp in employees:
    if emp["department"] == "數據工程師":
        print(f'{emp["name"]}是技術人員')
    elif emp["department"] == "行銷" or emp["department"] == "業務":
        print(f'{emp["name"]}是業務相關人員')
    else:
        print(f'{emp["name"]}是其他部門')
    