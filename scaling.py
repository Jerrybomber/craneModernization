potentiometer_value = 8250
potentiometer_value_min = 3000
potentiometer_value_max = 13500
reach_max = 28
reach_min = 9

potentiometer_range = potentiometer_value_max - potentiometer_value_min

scaled_value = ((potentiometer_value - potentiometer_value_min) / potentiometer_range) * (reach_max - reach_min) + reach_min

print(scaled_value)
