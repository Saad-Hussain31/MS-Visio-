def earned_amount(duration):
    if duration < 1:
        print("INVALID INPUT!")
    else:
        amount = 1
        total = 0
        for i in range(duration):
            print(amount/100)
            total = total + amount
            amount = amount*2
        return total/100


print(earned_amount(10))
print(earned_amount(45))
