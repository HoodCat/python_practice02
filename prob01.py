money = int(input("금액: "))
kind_of_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
print()

for m in kind_of_money:
    print(str(m) + "원: " + str(money//m) + "개")
    money %= m