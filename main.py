def filter_long_names(product_names):
    """Filters product names with length greater than or equal to 5."""
    return [name for name in product_names if len(name) >= 5]

def get_product_names():
    """Gets product names from user input."""
    product_names = []
    while True:
        name = input("Enter a product name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        product_names.append(name)
    return product_names

product_names = get_product_names()

# Validation: Ensure at least one product name is entered
while not product_names:
    print("Please enter at least one product name.")
    product_names = get_product_names()

long_names = filter_long_names(product_names)

# Output Formatting
print("\nTotal number of product names entered:", len(product_names))
print("Number of product names with at least 5 characters:", len(long_names))
print("Long product names:", long_names)
