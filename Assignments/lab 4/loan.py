def loan(total_amount, percent_per_year):
    amount_paid_after_3yr =round(total_amount*(percent_per_year/100)*3)
    total_time_to_pay = round(100/percent_per_year, 2)
    return amount_paid_after_3yr, total_time_to_pay

print(loan(10000, 10))
print(loan(200000, 23))
