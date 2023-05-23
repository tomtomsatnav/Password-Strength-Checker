def passwordStrength(givenPassword):
    # Check if the password length is less than 8 characters
    if len(givenPassword) < 8:
        return 0  # Return 0 to indicate a weak password
    
    # Initialise the score variable
    score = 0

    # Check if the password has at least 8 unique characters
    if len(set(givenPassword)) >= 8:
        score += 1  # Increase the score by 1

    # Check for consecutive repeating characters in the password
    for i in range(len(givenPassword) - 2):
        if givenPassword[i] == givenPassword[i + 1] == givenPassword[i + 2]:
            score += 1  # Increase the score by 1
            break

    # Check if the password contains at least one digit
    if any(char.isdigit() for char in givenPassword):
        score += 1  # Increase the score by 1

    return score  # Return the final score indicating password strength


# Input a password from the user
password = input("Enter a password: ")

# Call the passwordStrength function to check the password
passwordScore = passwordStrength(password)

# Print the score indicating the password strength
print("Password strength score:", passwordScore)