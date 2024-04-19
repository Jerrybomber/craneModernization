# Define a table for weight in kilograms and corresponding maximum reach in centimeters
weight_table = [15.0, 15.5, 16.5, 17.5, 18.5, 20.0, 22.0, 23.5, 25.5, 27.5, 30.0]
reach_table = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]

# Function to calculate maximum weight based on reach
def calculate_weight(reach):
    # Initialize maximum weight
    max_weight = 0
    
    # If reach is less than or equal to 18, set maximum weight to 30
    if reach <= 18:
        max_weight = 35
        return max_weight

    # If reach is greater than or equal to 28, set maximum weight to 15
    if reach >= 28:
        max_weight = 15
        return max_weight

    # Iterate through reach_table to find the correct range
    for i in range(len(reach_table)-1):
        if reach_table[i] >= reach >= reach_table[i+1]:
            reach1 = reach_table[i]
            reach2 = reach_table[i+1]
            weight1 = weight_table[i]
            weight2 = weight_table[i+1]
            break

    # Calculate maximum weight using the formula
    max_weight = weight1 + ((reach - reach1) * (weight2 - weight1)) / (reach2 - reach1)

    return max_weight


def calculate_momentti(max_weight, used_weight):
   # Calculate momentti and return as a percentage
   momentti = (used_weight / max_weight) * 100
   if momentti > 100:
       return 101
   return momentti

# Set variables for weight (paino) and used reach (ulottuma)
paino = 31
ulottuma = 17

# Calculate maximum reach for the given weight
max_weight = calculate_weight(ulottuma)

# Calculate momentti based on maximum reach and used reach
momentti = calculate_momentti(max_weight, paino)

# Print the results
print(f"Weight: {paino} t")
print(f"Used Reach: {ulottuma} m")
print()
print(f"Maximum Weight: {max_weight} t")

# Print momentti if it is a number (int or float)
if isinstance(momentti, (int, float)):
   print(f"Momentti: {momentti:.1f}%")
else:
   print(momentti)