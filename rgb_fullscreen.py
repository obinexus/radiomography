import matplotlib.pyplot as plt
import math
from matplotlib.patches import Wedge
import colorsys

# Spectrum circle: 0° = Radio waves (origin), moving counterclockwise
# Approximate angle mappings based on speaker's description
spectrum_angles = {
    'Radio': 0,
    'Microwave': 30,
    'Infrared': 60,
    'Red': 90,         # 0 hops
    'Orange': 110,
    'Yellow': 130,
    'Green': 160,      # ~2 left hops
    'Blue': 200,       # 2 left + 1 right → net ~2 left
    'Indigo': 230,
    'Violet': 260,
    'UV': 300,
    'X-Ray': 330,
}

# Hop-based color derivation (simplified from speaker's rules)
def hops_to_color(hops_left, hops_right):
    net_hops = hops_left - hops_right
    if net_hops <= 0:
        return "Red" if abs(net_hops) == 0 else "Orange/Yellow"
    elif net_hops == 1 or net_hops == 2:
        return "Green"
    elif net_hops >= 2:
        return "Blue"
    return "Unknown"

# Test hop examples from transcript
print("Hop-based color resolution:")
print(hops_to_color(0, 0))        # → Red
print(hops_to_color(2, 0))        # → Green
print(hops_to_color(2, 1))        # → Blue (2L 1R)
print(hops_to_color(1, 1))        # → Red/Orange

# Polar visualization: Electromagnetic spectrum wheel
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
ax.set_theta_offset(math.radians(90))  # Start at top (Red visible)

colors = {
    'Radio': 'gray', 'Microwave': 'darkgray', 'Infrared': 'red',
    'Red': 'red', 'Orange': 'orange', 'Yellow': 'yellow',
    'Green': 'green', 'Blue': 'blue', 'Indigo': 'indigo',
    'Violet': 'violet', 'UV': 'purple', 'X-Ray': 'black'
}

for name, angle in spectrum_angles.items():
    theta = math.radians(angle)
    ax.annotate(name, (theta, 1.2), fontsize=10, ha='center')
    wedge = Wedge((0, 0), 1.3, angle - 15, angle + 15, facecolor=colors.get(name, 'white'), edgecolor='black', alpha=0.6)
    ax.add_patch(wedge)

ax.set_title("Radio Sensor System: Electromagnetic Spectrum as Polar Hop Map\n(0° = Radio Origin → Counterclockwise to Visible Light)", 
             va='bottom', pad=30)
ax.set_rlim(0, 1.5)
ax.grid(True)
plt.show()

# Bonus: Generate RGB value from angle (HSV → RGB)
def angle_to_rgb(angle_deg):
    hue = angle_deg / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r*255), int(g*255), int(b*255))

print("\nSample RGB from spectrum angles:")
for color, angle in [('Red', 90), ('Green', 160), ('Blue', 200)]:
    rgb = angle_to_rgb(angle)
    print(f"{color} ({angle}°): RGB{rgb}")
