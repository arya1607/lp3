def fractional_knapsack(weights, values, capacity):
    n = len(weights)

    # Create items with:
    # (item number, weight, value, value/weight ratio)
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((i + 1, weights[i], values[i], ratio))

    # Sort items according to value/weight ratio
    # in descending order
    items.sort(key=lambda x: x[3], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    print("\nItems sorted by Value/Weight Ratio:")
    print("Item\tWeight\tValue\tRatio")
    for item, weight, value, ratio in items:
        print(f"{item}\t{weight}\t{value}\t{ratio:.2f}")

    print("\nSelection of Items:")
    print("Item\tWeight Taken\tFraction\tValue Obtained")

    for item, weight, value, ratio in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take the complete item
            weight_taken = weight
            fraction = 1
            value_obtained = value
        else:
            # Take only the required fraction
            fraction = remaining_capacity / weight
            weight_taken = remaining_capacity
            value_obtained = value * fraction

        total_value += value_obtained
        remaining_capacity -= weight_taken

        print(
            f"{item}\t{weight_taken:.2f}\t\t"
            f"{fraction:.2f}\t\t{value_obtained:.2f}"
        )

    return total_value


# Main Program
n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    weight = float(input(f"Enter weight of item {i + 1}: "))
    value = float(input(f"Enter value of item {i + 1}: "))
    weights.append(weight)
    values.append(value)

capacity = float(input("Enter the capacity of the knapsack: "))

# Calculate maximum value
max_value = fractional_knapsack(weights, values, capacity)

print("\nMaximum value that can be obtained:", max_value)

print("\nComplexity Analysis:")
print("Time Complexity : O(n log n)")
print("Space Complexity : O(n)")
