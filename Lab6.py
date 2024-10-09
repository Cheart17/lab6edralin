age = int(input("Please Enter your age: "))
membership_status = input("Are you a member or a Non-Member? (Enter 'Member' or 'Non-member'): ")

if age < 18:
    if membership_status == "Member":
        fee = 450
    else:
        fee = 650
elif 18 <= age <= 65:
    if membership_status == "Member":
        fee = 550
    else:
        fee = 750
elif age > 65:
    if membership_status == "Member":
        fee = 400
    else:
        fee = 600
else:
    fee = None 
    

if fee is not None:
    print(f"The registration fee is {fee} pesos.")
else: 
    print("Invalid input.")    