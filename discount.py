def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount
    is 20% or higher. Otherwise, returns the original price.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.

    Returns:
    - float: The final price after applying the discount or the original price.
    """
    
    if discount_percent >= 20:
        # Apply discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
