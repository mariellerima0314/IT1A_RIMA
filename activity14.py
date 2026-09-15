#age (integer)
#is_employed (boolean)
#credit_score (integer)
#annual_income (float)
#has collateral (boolean)

age = int(input("Enter your age: "))
is_employed = bool(input("Are you employed? (True/False): "))
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = bool(input("Do you have collateral? (True/False): "))

#High_Credit 
if age >= 21 and is_employed == True:
    print("Accepted Baseline Criteria")
    if credit_score >= 750: #tier1
        print("You have a high credit score. ")
        if annual_income >= 100000:
            print("You have a high annual income. ")
            base_rate = 4.5
            print("Your base interest rate is: ", base_rate)
        else: 
            base_rate = 5.0
            print("Your base interest rate is: ", base_rate)
elif credit_score >= 600 and credit_score < 750: #tier2
    print("You have a fair credit score. ")
    if has_collateral == True:
        print("You have collateral. ")
        base_rate = 7.0
        print("Your base interest rate is: ", base_rate)
    elif annual_income <= 40000:
        print("Low annual income. ")
        base_rate = 9.0
        print("Your base interest rate is: ", base_rate)
    else: 
        base_rate = 8.0
        print("Your base interest rate is: ", base_rate)

else:
    print("Rejected: Credit score too low.")
