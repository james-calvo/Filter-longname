def filter_long_names(product_names):
    """Filters product names with length greater than or equal to 5."""
    return [name for name in product_names if len(name) >= 5]

product_names = ["Shirt", "Headphones", "Monitor", "Cable"]
long_names = filter_long_names(product_names)
print(long_names)  # Output: ['Shirt', 'Headphones', 'Monitor']
