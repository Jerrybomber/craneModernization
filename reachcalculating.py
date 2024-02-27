weight_table = [15.0, 15.5, 16.5, 17.5, 18.5, 20.0, 22.0, 23.5, 25.5, 27.5, 30.0]
reach_table = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]

def calculate_reach(weight):
    max_reach = 0
    if weight < 15:
        max_reach = 28
        return max_reach
    
    if 30 <= weight <= 35:
        max_reach = 18
        return max_reach
    
    if weight > 35:
        max_reach = 0
        return max_reach
    
    for i in range(len(weight_table)-1):
        if weight_table[i] <= weight <= weight_table[i+1]:
            weight1 = weight_table[i]
            weight2 = weight_table[i+1]
            reach1 = reach_table[i]
            reach2 = reach_table[i+1]
            break
    
    max_reach = max(reach1, reach2) + ((weight - weight1) * (min(reach1, reach2) - max(reach1, reach2))) / (weight2 - weight1)

    return max_reach
"""
for i in weight_table:
    print("Maksimi ulottuma painolla", i, "on", calculate_reach(i))
"""

paino = 34 
print("Maksimi ulottuma painolla", paino, "on", calculate_reach(paino))