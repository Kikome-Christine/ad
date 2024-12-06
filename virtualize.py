import matplotlib.pyplot as plt

# Product data
original_price = 500  # Base price per item
discount = 10  # Discount percentage
quantity = 2  # Number of items

# Calculate data
total_before_discount = original_price * quantity
total_after_discount = total_before_discount - (total_before_discount * discount / 100)

# Visualization
categories = ['Original Price', 'Price After Discount']
values = [total_before_discount, total_after_discount]

plt.bar(categories, values, color=['blue', 'green'])
plt.title('Price Before and After Discount')
plt.xlabel('Price Categories')
plt.ylabel('Amount ($)')
plt.show()
