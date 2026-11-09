# Reflection 1
# I would use .get() when a key might be missing because it lets me provide
# a default value without crashing the program. I would use bracket notation
# when I expect the key to exist and want an error if it does not.

# Reflection 2
# This reminds me of using SUMIF or a PivotTable in Excel to total values by category.
# Python can be more useful for large datasets because it can automate the process
# and handle much larger amounts of data.


# Exercise 1

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 4250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the dictionary keys.
for key in customer:
    print(key)


# Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", customer["tier"])
print("Discount:", f"{discount_rate:.0%}")
print("Final price:", f"${final_price:.2f}")


# Exercise 6

customers = [
    {
        "name": "Alice",
        "tier": "platinum"
    },
    {
        "name": "Bob",
        "tier": "gold"
    },
    {
        "name": "Charlie",
        "tier": "silver"
    }
]

purchase_price = 300

for customer_record in customers:
    discount_rate = tier_discounts.get(customer_record["tier"], 0)
    discount_amount = purchase_price * discount_rate

    print(
        f"{customer_record['name']}: "
        f"{customer_record['tier']}, "
        f"discount ${discount_amount:.2f}"
    )


# Exercise 7

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
    