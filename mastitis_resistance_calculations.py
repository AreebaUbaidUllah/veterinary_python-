print("Mastitis Antibiotic Resistance Analysis")
print("----------------------------------------")

# Data from laboratory testing
total_samples = 70
resistant_samples = 20

# Calculate resistance percentage
resistance_percentage = (resistant_samples / total_samples) * 100

# Display results
print("Total Samples Tested:", total_samples)
print("Resistant Samples:", resistant_samples)
print("Resistance Percentage:", round(resistance_percentage, 2), "%")

# Classify resistance level
if resistance_percentage < 20:
    print("Resistance Level: Low")
elif resistance_percentage <= 50:
    print("Resistance Level: Moderate")
else:
    print("Resistance Level: High")

print("\nConclusion:")
print("Moderate resistance observed in mastitis cases.")
print("Antibiotic selection should be based on sensitivity testing.")