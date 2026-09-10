#GLOBAL FREIGHT CALCULATOR

#INPUTS
sender_name = input("Sender Name:	")

type_of_Item = input("Type of Item:	")

is_Fragile = bool(input("Is the Item Fragile?"))

if is_Fragile == True and is_Fragile == False:
	print("Handle with care")
else:
	print("Not Fragile")

weight_of_Item = float(input("Weight of the product (kg):	"))

distance = float(input("How far (km) is your location from where the product is ordered?:	"))

is_express = input("Is it express? (True/False): ") == "True"

is_international = input("Is it international? (True/False): ") == "True"

# 1. Calculate Base Cost
base_cost = (weight_of_Item  * 2.50) + (distance * 0.15)

# 2. Evaluate pricing tiers in strict order
if weight_of_Item <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight_of_Item > 20):
    total = (base_cost * 1.20) + 25

elif weight_of_Item > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost

# Output
print("\n--- Shipping Summary ---")
print("Sender:", sender_name)
print("Item:", type_of_Item)
print("Fragile:", is_Fragile)
print("Base Cost: ${:.2f}".format(base_cost))
print("Total Shipping Charge: ${:.2f}".format(total))


