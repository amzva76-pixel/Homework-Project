import math
import random

print("🌟 Welcome to the Trigonometric Explorer 🌟")

choice = input("Press 'Enter' for a random angle, or type a number (0-360): ")

if choice == "":
    angle = random.randint(0, 360)
else:
    angle = int(choice)


rad = math.radians(angle)

s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

print("-" * 30)
print(f"📍 Target Angle: {angle}°")

print(f"📐 Height (Sine):   {round(s, 3)}  {'⬆️' if s > 0 else '⬇️'}")
print(f"↔️  Width (Cosine):  {round(c, 3)}  {'➡️' if c > 0 else '⬅️'}")

if abs(c) < 0.001: 
    print("🎢 Slant (Tangent): ⚠️ Super Steep! (Undefined)")
else:
    print(f"🎢 Slant (Tangent): {round(t, 3)}")
print("-" * 30)

if angle > 0 and angle < 90:
    print("Quadrant 1: Everything is positive! 🌈")
elif angle >= 90 and angle < 180:
    print("Quadrant 2: You are high up, but moving left! ⬅️")