# Percent Increase Bonus Activity

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price

op = float(100.5)
print('The Original Price of Apple Stock is', op)

# Create float variable for current_price

cp = float(145.5)
print('The Current Price of Apple Stock is', cp)
# Calculate difference between current_price and original_price

increase = cp - op
print('The Increase in price of Apple Stock is', increase)
# Calculate percent_increase

PI = increase / op * 100
print('The Percent Increase in Apple Stock Price is', PI)

# Print percent_increase to 2 decimal places using string formatting

print('The Rounde Percent increase is', round(PI, 2))
