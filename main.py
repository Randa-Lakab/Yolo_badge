# Currency Converter: Algerian Dinar (DZD) -> US Dollar (USD)

print("=== Currency Converter DZD -> USD ===")

# Exchange rate (example: 1 USD = 220 DZD)
exchange_rate = 220  

# Ask the user for amount in DZD
dzd = float(input("Enter amount in Algerian Dinar (DZD): "))

# Convert to USD
usd = dzd / exchange_rate

# Show result
print(f"{dzd} DZD = {usd:.2f} USD")
