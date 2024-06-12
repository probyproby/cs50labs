'''
while True:
    Initialize Amount Due = 50
    prompt user to insert coin = int()
    calculate (Amount due - Inserted coin)
    return Amount Due if amount due != 0:
        else return "change owed = 0"


amount = 50
print("Amount Due: ", amount)

while True:
    coin1 = 25
    coin2 = 10
    coin3 = 5

    insert_coin = int(input("Insert Coin: "))
    if insert_coin == coin1:
        amount_due0 = amount - insert_coin
        print("Amount Due: ", amount_due0)
    elif insert_coin == coin2 :
        amount1 = amount_due0 - insert_coin
        print("Amount Due: ", amount1)
    elif insert_coin == coin3:
        amount_due1 = amount1 - insert_coin
        print("Amount Due: ", amount_due1)
    elif amount <= 0:
        print("Change Owed: 0")
    else:
        break
'''

#amount = 50
#print("Amount Due: ", amount)

#while range(50):
#    coin1 = 25
#    coin2 = 10
#    coin3 = 5

#    insert_coin = int(input("Insert Coin: "))
#    if insert_coin == coin1:
#        amount_due0 = amount - insert_coin
#        print("Amount Due: ", amount_due0)
#    elif insert_coin == coin2 :
#        amount1 = amount_due0 - insert_coin
#        print("Amount Due: ", amount1)
#    elif insert_coin == coin3:
#        amount_due1 = amount1 - insert_coin
#        print("Amount Due: ", amount_due1)
#    elif amount <= 0:
#        print("Change Owed: 0")
#    else:
#        break

amount = 50

while amount > 0:
    print("Amount Due:", amount)
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount -= insert_coin
    elif amount == 0:
        break

print("Change Owed: 0")