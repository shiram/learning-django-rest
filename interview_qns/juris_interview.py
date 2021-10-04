"""
$2 - bread
$3 - noodles
$5 - soft drink
$8 - meal set A 
$10 - meal set B
"""

products = {
    'bread': 2,
    'noodles': 3,
    'soft drink': 5,
    'meal set A': 8,
    'meal set B': 10
}

my_budget = 5
items_to_buy = []
for item in products:
    if products[item] <= my_budget:
        items_to_buy.append(item)

print(items_to_buy)
