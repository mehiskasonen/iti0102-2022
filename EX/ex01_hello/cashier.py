"""Cha-ching."""


amount = int(input("Enter a sum: "))
while not int(amount) in range(1, 101):
    amount = int(input("Enter a sum between 1 and 100: "))
b = amount // 50
stock_b = amount % 50
c = stock_b // 20
stock_c = stock_b % 20
d = stock_c // 10
stock_d = stock_c % 10
e = stock_d // 5
stock_e = stock_d % 5
f = stock_e // 1
stock_f = stock_e % 1
coins = (b + c + d + e + f)
print(f"Amount of coins needed: {coins}")
