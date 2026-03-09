from itertools import combinations

# Transaction dataset
transactions = [
    {"laptop", "mouse"},
    {"laptop", "keyboard"},
    {"mouse", "keyboard"},
    {"laptop", "mouse", "keyboard"},
    {"laptop", "mouse"}
]

min_support = 2

# Step 1: Count single items
item_counts = {}

for transaction in transactions:
    for item in transaction:
        if item not in item_counts:
            item_counts[item] = 1
        else:
            item_counts[item] += 1

print("Frequent 1-itemsets:")
for item, count in item_counts.items():
    if count >= min_support:
        print(item, ":", count)


# Step 2: Generate 2-itemsets
pair_counts = {}

for transaction in transactions:
    pairs = combinations(transaction, 2)
    for pair in pairs:
        pair = tuple(sorted(pair))
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1

print("\nFrequent 2-itemsets:")
for pair, count in pair_counts.items():
    if count >= min_support:
        print(pair, ":", count)