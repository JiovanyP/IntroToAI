from itertools import combinations

transactions = [
    {"bread", "milk"},
    {"bread", "diaper", "beer", "eggs"},
    {"milk", "diaper", "beer", "coke"},
    {"bread", "milk", "diaper", "beer"},
    {"bread", "milk", "diaper", "coke"}
]

min_support = 2

# Count single items
item_count = {}

for transaction in transactions:
    for item in transaction:
        item_count[item] = item_count.get(item, 0) + 1

print("Frequent 1-itemsets:")
for item, count in item_count.items():
    if count >= min_support:
        print(item, ":", count)