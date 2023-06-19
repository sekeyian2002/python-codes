def is_palindrome(string):
    # Remove any spaces and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")