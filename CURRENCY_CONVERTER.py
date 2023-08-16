def convert_currency(amount, currency_code):
    conversion_rates = {
        'USD': 1.18,  # example conversion rates, you can update them with actual rates
        'EUR': 1.00,
        'GBP': 1.39,
        'JPY': 0.0096,
    }

    if currency_code not in conversion_rates:
        return "Error: Invalid currency code."

    converted_amount = amount * conversion_rates[currency_code]
    return converted_amount


# Prompt the user for input
input_amount = float(input("Enter an amount: "))
input_currency = input("Enter the currency code: ")

# Call the convert_currency function
converted_amount = convert_currency(input_amount, input_currency)

# Print the original amount and converted amount
print(f"Original amount: {input_amount} {input_currency}")
print(f"Converted amount: {converted_amount} {input_currency}")





 
    