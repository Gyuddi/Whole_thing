money=int(input("투입한 돈:"))
price=int(input("물건값:"))
less=money-price
five=less//500
one=less%500
print("거스름돈:",less)
print("500원의 개수:",five)
print("100원의 개수:",one)
