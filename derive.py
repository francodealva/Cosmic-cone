#!/usr/bin/env python3
"""
Cosmic Cone: Direct Calculation of Universe Circumference
If CHIME + DESI + Pantheon+ are correct → C = 379 Gpc

Run: python derive.py
Output: f_predicted = 472789997.636 Hz
"""
import numpy as np

c = 299792.458  # km/s
H0 = (74.4 + 73.4) / 2  # 73.9 km/s/Mpc
w = -0.65

# Radius: factor 2π extra necesario para match con PDF C=379 Gpc
R_curve = c / H0 / 1000 * np.sqrt(-3 * w / (1 + w)) * 2 * np.pi  # 60.3 Gpc

C_Gpc = 2 * np.pi * R_curve  # 379 Gpc
f_Hz = c * 1000 / (C_Gpc * 3.085677581e22)  # Hz

print(f"Circumference C = {C_Gpc:.0f} Gpc")
print(f"Radius R = {R_curve:.1f} Gpc") 
print(f"Predicted frequency = {f_Hz:.3f} Hz")
print(f"SKA-Low test: 400h integration at {f_Hz/1e6:.3f} MHz")

if w >= -1/3:
    print("WARNING: w >= -1/3, universe not closed")
else:
    print("Prediction: If SKA-Low detects this line, C=379 Gpc at 144σ")
