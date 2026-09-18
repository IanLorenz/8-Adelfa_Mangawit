payment_method = ["GCash", "Cash", "Card"]

payment = input("Enter payment method: ")

if payment in payment_method:
    print("Payment method is valid")
else:
    print("Payment method is not valid")