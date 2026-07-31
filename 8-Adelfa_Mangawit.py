item1_name = input("What item is the customer buying?")
price_per_unit1 = float(input("Enter price per unit (₱): "))
quantity = int(input("How many units?"))

item2_name = input("What item is the customer buying?")
price_per_unit2 = float(input("Enter price per unit (₱): "))
quantity = int(input("How many units?"))

subtotal = price_per_unit1 + price_per_unit2 * quantity
vat_rate = 0.12
vat_amount = subtotal * vat_rate
total_with_vat = subtotal + vat_amount

print("===================================")
print("    SARI-SARI STORE RECEIPT")
print("===================================")
print(f"Item: {item1_name}")
print(f"Price/Unit: ₱{price_per_unit1}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₱{subtotal:.2f}")
print(f"Item: {item2_name}")
print(f"Price/Unit: ₱{price_per_unit2}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print("===================================")
print(f"Total: ₱{total_with_vat:.2f}")
print("===================================")
print("Salamt! Come Again!")