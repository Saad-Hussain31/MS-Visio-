def greatest_number(first, second, third):
    if first >= second:
        if first >= third:
            return first
        else:
            return third
    else:
        if second >= third:
            return second
        else:
            return third


print(greatest_number(5, 252, 25))
print(greatest_number(333, 0, 333))
