"""
Conditionally Yours

Pseudocode:


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price

op = 100

# Create integer variable for current_price

cp = 150

# Create float for threshold_to_buy

if cp > op:
    print('BUY APPLE STOCK NUMBNUTS!')

# Create float for threshold_to_sell

if cp < op:
    print('SELL THE STOCK NUMBNUTS')

# Create float for portfolio balance

Stock_Amount = 10
Portfolio_Original = Stock_Amount * op
Portfolio_Balance = Stock_Amount * cp

if cp > op:
    print("You've Made", Portfolio_Balance-Portfolio_Original,"Dollars on your Intial Investment!")


# Create float for balance check


# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price


# Calculate percent increase


# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price


# Print percent increase


# Determine if stock should be bought or sold


# Print recommendation
print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance variable as a float


# Declare balance_check variable
balance_check = balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${balance} in excess equity available in your portfolio.")

# IF-ELSE Logic to determine recommendation based off of balance check
