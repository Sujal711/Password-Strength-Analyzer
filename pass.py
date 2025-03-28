import re  

def password_checker(pwd):
    """
    Evaluates the strength of a given password.
    It analyzes length, character diversity, and common weaknesses.
    """

    # Initializing evaluation score
    rating = 0
    recommendations = []

    # Checking password length
    length = len(pwd)
    if length >= 12:
        rating += 2
    elif 8 <= length < 12:
        rating += 1
    else:
        recommendations.append("Make sure your password has at least 12 characters.")

    # Verifying presence of uppercase letters
    if any(char.isupper() for char in pwd):
        rating += 1
    else:
        recommendations.append("Add at least one uppercase letter.")

    # Verifying presence of lowercase letters
    if any(char.islower() for char in pwd):
        rating += 1
    else:
        recommendations.append("Add at least one lowercase letter.")

    # Checking for numerical digits
    if any(char.isdigit() for char in pwd):
        rating += 1
    else:
        recommendations.append("Include at least one digit.")

    # Checking for special characters
    special_chars = "!@#$%^&*()_+=-[]{};:'\",.<>?/|\\"
    if any(char in special_chars for char in pwd):
        rating += 1
    else:
        recommendations.append("Use at least one special symbol.")

    # Checking for common weak passwords
    weak_passwords = {"password", "123456", "qwerty", "admin", "letmein"}
    if pwd.lower() in weak_passwords:
        rating -= 1
        recommendations.append("Avoid using easily guessed passwords.")

    # Assigning password strength
    if rating >= 5:
        security_level = "Strong"
    elif 3 <= rating < 5:
        security_level = "Moderate"
    else:
        security_level = "Weak"

    # Displaying the results
    print("\n🔹 Password Strength Report 🔹")
    print(f"🔹 Security Level: {security_level} ({rating}/5)")

    if recommendations:
        print("\n🔹 Tips for a Stronger Password:")
        for tip in recommendations:
            print(f"  - {tip}")

# Request user input
while True:
    user_pwd = input("\nEnter your password (or type 'exit' to quit): ")
    if user_pwd.lower() == "exit":
        print("Goodbye! Stay secure. 🔒")
        break
    password_checker(user_pwd)
