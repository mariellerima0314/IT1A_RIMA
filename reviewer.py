#Inputs:
#owner_age (integer)
#monthly_revenue (float)
#credit_score (integer)
#years_in_business (float)
#has_defaults (boolean)
#collateral_name (string)
#collatreal_value (float)

age = int(input("Enter your age: "))
monthly_revenue = float(input("Enter your monthly revenue: ")) 
cc = int(input("Enter your credit score: "))
yrs = float(input("Enter your years in business: "))
has_defaults = bool(input("Do you have any defaults?     "))
collateral_name = input("Enter the name of your collateral: ")
collateral_value = float(input("Enter the value of your collateral: "))

#Baseline Criteria:
max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and yrs >= 2:
    print("Accepted Baseline Criteria")
    if cc >= 720: #tier1
        print("You have a high credit score. ")
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 50000:
            print("You have a high monthly revenue. ")
            base_fee = max_loan * 0.015
            print("Your base interest rate is: ", base_fee)
        else:
            print("You have a low monthly revenue. ")
            base_fee = max_loan * 0.025
            print("Your base interest rate is: ", base_fee)
    elif cc >= 620 and cc < 720: #tier 2
        print("You have a fair credit score. ")
        max_loan = monthly_revenue * 1.5
        if yrs >= 5:
            print("You have been in business for a long time. ")
            base_fee = max_loan * 0.02
            print("Your base interest rate is: ", base_fee)
        else: 
            print("You have been in business for a short time. ")
            base_fee = max_loan * 0.035
            print("Your base interest rate is: ", base_fee)

        #revenue
        if monthly_revenue >= 50000:
            print("You have a high monthly revenue. ")
            base_fee = max_loan * 0.015
            print("Your base interest rate is: ", base_fee)
        else:
            print("You have a low monthly revenue. ")
            base_fee = max_loan * 0.025
            print("Your base interest rate is: ", base_fee)

        #collateral
        if collateral_value >= max_loan:
            print("You have sufficient collateral", collateral_value, "is sufficient.")
        else:
            print("You have insufficient collateral", collateral_value, "is insufficient.")

        #surcharge
        if collateral_value % 5000 != 0:
            base_fee += 250
            print("Additional charge added to Base Fee, total base fee is", base_fee)
        else:
            print("Collateral divisible by 5000")

            
    elif cc < 620: #tier 3
        print("Rejected: Credit score too low.")
    else:
        print("Invalid")

else:
    print("Baseline Failed")

