# Ask the user for a temperature in Fahrenheit and convert it to a decimal number (float)
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert the temperature from Fahrenheit to Celsius using the conversion formula
celsius = (fahrenheit - 32) * 5 / 9

# Print the final result rounded to one decimal place using an f-string
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")
