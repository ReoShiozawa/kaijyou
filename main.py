def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 入力を受け取る
try:
    num = int(input("数字を入力してください: "))
    if num < 0:
        print("負の数の階乗は計算できません。")
    else:
        print(f"{num} の階乗は {factorial(num)} です。")
except ValueError:
    print("有効な整数を入力してください。")
