import math

def get_circumference(radius):
    """Calculates circumference given a radius."""
    return 2 * math.pi * radius


try:
    r = float(input("Enter the radius of the circle: "))
    
    if r < 0:
        print("Radius cannot be negative.")
    else:
        
        circumference = get_circumference(r)
        print(f"The circumference of the circle is: {circumference:.2f}")
except ValueError:
    print("Invalid input. Please enter a numerical value.")
