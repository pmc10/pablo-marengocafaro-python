def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Test with example values using f-strings and round to one decimal place
c1, c2 = 0, 100
f1 = 72

print(f"{c1}°C = {celsius_to_fahrenheit(c1):.1f}°F")
print(f"{c2}°C = {celsius_to_fahrenheit(c2):.1f}°F")
print(f"{f1}°F = {fahrenheit_to_celsius(f1):.1f}°C")
