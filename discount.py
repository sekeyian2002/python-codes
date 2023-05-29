purchase_amount = float(input("Enter the amount of purchase in Ksh: "))
if purchase_amount > 1000:
    discount = purchase_amount * 0.05
    discounted_amount = purchase_amount - discount
    print(f"Your purchase amount of {purchase_amount} Ksh is eligible for a 5% discount.")
    print(f"Your discounted amount payable is {discounted_amount} Ksh.")
else:
    print("Your purchase amount is not eligible for a discount.")
    print(f"Your amount payable is {purchase_amount} Ksh.")
