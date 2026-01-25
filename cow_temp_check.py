# Cow body temperatures in Fahrenheit
cow_temperatures_F = [103.4, 101.6, 102.0, 103.6, 101.6, 104.0, 102.2, 100.4, 103.1, 101.8]
# Fever threshold in Fahrenheit
fever_threshold = 102.5
# Check each cow
for c in range(10):
    temp = cow_temperatures_F[c]
    if temp > fever_threshold:
        print("Cow", c+1, ": Fever detected (", temp, "°F )")
    else:
        print("Cow", c+1, ": Temperature normal (", temp, "°F )") 