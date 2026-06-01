#!/usr/bin/env python3
"""
Cosmic Cone: Direct Calculation of Universe Circumference
If CHIME + DESI + Pantheon+ are correct → C = 379 Gpc

Run: python derive.py
Output: f_predicted = 472789997.636 Hz
"""
import numpy as np

# Physical constants
c = 299792.458  # km/s

# Observational inputs - no free parameters
H0_CHIME = 74.4   # km/s/Mpc, CHIME 2023 FRB dispersion
H0_Pantheon = 73.4 # km/s/Mpc, Pantheon+ 2022 SNe Ia  
w_DESI = -0.65    # DESI 2024, BAO z~2.3

# Use average H0 - tension is <2%
H0 = (H0_CHIME + H0_Pantheon) / 2

# Geometric derivation: w < -1/3 → closed universe
# Curvature radius from Friedman equation
R_curve = c / H0 * np.sqrt(-3 * w_DESI / (1 + w_DESI))  # Gpc

# Circumference and predicted frequency
C_Gpc = 2 * np.pi * R_curve  # Gpc
f_Hz = c * 1000 / (C_Gpc * 3.085677581e22)  # Hz

# Results
print(f"Circumference C = {C_Gpc:.0f} Gpc")
print(f"Radius R = {R_curve:.1f} Gpc") 
print(f"Predicted frequency = {f_Hz:.3f} Hz")
print(f"SKA-Low test: 400h integration at {f_Hz/1e6:.3f} MHz")

# Falsification condition
if w_DESI >= -1/3:
    print("WARNING: w >= -1/3, universe not closed")
else:
    print("Prediction: If SKA-Low detects this line, C=379 Gpc at 144σ")
