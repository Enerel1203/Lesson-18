import math

angle = float(input("Enter an angle in degrees: "))

radian = math.radians(angle)

sin_val = round(math.sin(radian), 4)
cos_val = round(math.cos(radian), 4)
tan_val = "undefined" if cos_val == 0 else round(math.tan(radian), 4)

print(f"\nTrigonometric values for {angle}°:")
print(f"sin({angle}) = {sin_val}")
print(f"cos({angle}) = {cos_val}")
print(f"tan({angle}) = {tan_val}")
