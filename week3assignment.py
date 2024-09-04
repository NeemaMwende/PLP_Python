def calculate_discount(price, discount_percent):
    # Calculate the final price after applying the discount
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price
    return final_price

def main():
    try:
        # Prompt the user for input
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Use the calculate_discount function to get the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after discount is: ${final_price:.2f}")
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
