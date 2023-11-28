# Taking the number of countries that the user would like to enter
num_coun = int(input("Enter the number of countries you would like to enter: "))
# Defining a list called user_coun_in
user_coun_in = []

# Defining a for loop that iterate through the length of the user_coun_in list
for i in range(num_coun):
    # Taking input of all the countries
    user_in = input(f"Enter country #{i + 1}: ")
    # Appending the countries to user_coun_in list
    user_coun_in.append(user_in.lower())

# Removing all duplicate elements in the user_coun_in list
unique_countries = list(set(user_coun_in))

# Print the total length of the user_coun_in list
print(f"You have {len(unique_countries)} unique countries in your array")
