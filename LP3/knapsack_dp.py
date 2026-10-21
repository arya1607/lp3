def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items, dp


# Main Program
n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

# Solve the problem
max_value, selected_items, dp = knapsack(
    weights, values, capacity
)

# Display DP table
print("\nDynamic Programming Table:")
print("Item\\Capacity", end="\t")
for w in range(capacity + 1):
    print(w, end="\t")
print()

for i in range(n + 1):
    print(i, end="\t\t")
    for w in range(capacity + 1):
        print(dp[i][w], end="\t")
    print()

print("\nSelected Items:")
total_weight = 0
total_value = 0

for item in selected_items:
    total_weight += weights[item - 1]
    total_value += values[item - 1]
    print(
        f"Item {item}: "
        f"Weight = {weights[item - 1]}, "
        f"Value = {values[item - 1]}"
    )

print("\nTotal Weight:", total_weight)
print("Maximum Value:", max_value)

print("\nComplexity Analysis:")
print("Time Complexity : O(n * W)")
print("Space Complexity : O(n * W)")
