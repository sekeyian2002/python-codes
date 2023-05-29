age = int(input("Enter your age: "))
citizenship = input("Are you an east african  citizen?(kenya,uganda,tanzania) (yes or no): ")

if age >= 18 and citizenship.lower() == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")