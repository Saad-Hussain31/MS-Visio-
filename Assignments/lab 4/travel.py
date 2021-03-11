def travel_amount(current_package, increase_each_yr):
    years_for_price_get_double = round(100/increase_each_yr, 2)
    return years_for_price_get_double


print(travel_amount(1622600, 6.5))
print(travel_amount(234134243, 2.5))
