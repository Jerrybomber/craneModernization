# Define a table for weight in kilograms and corresponding maximum reach in centimeters
weight_table = [15.0, 15.5, 16.5, 17.5, 18.5, 20.0, 22.0, 23.5, 25.5, 27.5, 30.0]
reach_table = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]

# Function to calculate maximum reach based on weight
def calculate_reach(weight):
   # Initialize maximum reach
    max_reach = 0
   
   # If weight is less than 15 kg, set maximum reach to 28 cm
    if weight < 15:
       max_reach = 28
       return max_reach

   # If weight is between 30 and 35 kg, set maximum reach to 18 cm
    if 30 <= weight <= 35:
       max_reach = 18
       return max_reach

   # If weight is greater than 35 kg, set maximum reach to 0 cm
    if weight > 35:
       max_reach = 0
       return max_reach

   # Iterate through weight_table to find the correct range
    for i in range(len(weight_table)-1):
       if weight_table[i] <= weight <= weight_table[i+1]:
           weight1 = weight_table[i]
           weight2 = weight_table[i+1]
           reach1 = reach_table[i]
           reach2 = reach_table[i+1]
           break
    
    if reach1 > reach2:
       max_reach1 = reach1
       min_reach1 = reach2
    elif reach2 > reach1:
       max_reach1 = reach2
       min_reach1 = reach1
       
    
   # Calculate maximum reach using the formula
    max_reach = max_reach1 + ((weight - weight1) * (min_reach1 - max_reach1)) / (weight2 - weight1)

    return max_reach

# Function to calculate momentti based on maximum reach and used reach
def calculate_momentti(max_reach, used_reach):
   # Calculate momentti and return as a percentage
   momentti = (used_reach / max_reach) * 100
   if momentti > 100:
       return 101
   return momentti

# Set variables for weight (paino) and used reach (ulottuma)
paino = 35
ulottuma = 20

# Calculate maximum reach for the given weight
max_ulottuma = calculate_reach(paino)

# Calculate momentti based on maximum reach and used reach
momentti = calculate_momentti(max_ulottuma, ulottuma)

# Print the results
print(f"Weight: {paino} t")
print(f"Used Reach: {ulottuma} m")
print()
print(f"Maximum Reach: {max_ulottuma} m")

# Print momentti if it is a number (int or float)
if isinstance(momentti, (int, float)):
   print(f"Momentti: {momentti:.1f}%")
else:
   print(momentti)


