#Program to find if eligible for COVID-19 vaccine
family_number = int(input("Enter the number of family members in your household:"))

for i in range(family_number):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    if age >= 60:
        print("Get ready for vaccine and show your phboto id")
    if age < 60 >= 45:
        answer = bool(input("Do you have a comorbidity:"))
    if answer == "yes":
        print(name , "Get ready for the vaccine and show your photo id")
    if answer == "no":
        print(name , "Vaccination due in next phase")
