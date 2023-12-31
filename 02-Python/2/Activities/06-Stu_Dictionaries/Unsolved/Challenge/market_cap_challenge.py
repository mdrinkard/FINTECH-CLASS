# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)
banks = {
    "JP Morgan Chase" : 327,
    'Bank of America' : 302,
    'Citigroup': 173,
    'Wells Fargo': 273,
    'Goldman Sachs': 87,
    'Morgan Stanley': 72,
    'U.S. Bancorp': 83,
    'TD Bank': 108,
    'PNC Financial Services': 67,
    'Capital One': 47,
    'FNB Corporation': 4,
    'First Hawaiian Bank': 3,
    'Ally Financial': 12,
    'Wachovia': 145,
    'Republic Bancorp': .97
}
print(banks)

# @TODO: Change the market cap for 'Citigroup'

banks["Citigroup"] = 170
print(banks)

# @TODO: Add a new bank and market cap pair

banks["American Express"] = 33
print(banks)

# @TODO: Remove a bank from the dictionary

del banks["Wachovia"]
print(banks)

# @TODO: Initialize metric variables

total_market_cap = 0
banks_count = 0 
average = 0
largest_bank = 0
smallest_bank = 0

# @TODO: Initialize minimum key-value pair
for bank_name, market_cap in banks.items():
    print(f'Name = {bank_name} has market cap = {market_cap}')
    
    total_market_cap = total_market_cap + market_cap
    banks_count = banks_count + 1

print(total_market_cap)
print(banks_count)

# @TODO: Initialize maximum key-value pair




# Mega Cap: Firms with a market capitalization over $300 billion.
# Large Cap: Firms with a market capitalization over 10 billion. ...
# Mid Cap: A market capitalization between $2 and $10 billion.
# Small Cap: A market capitalization between $300 million and $2 billion.

# @TODO: Initialize market cap lists





# @TODO: Iterate over key-value pairs of the dictionary




    # @TODO: Calculate sum of market caps and number of banks in the dictionary



    # @TODO: Logic to determine min value and associated key







    # @TODO: Logic to determine max value and associated key




    # @TODO: Group banks by categories of market caps










# @TODO: Calculate average market cap of banks in the dictionary


# @TODO: Print the metrics
