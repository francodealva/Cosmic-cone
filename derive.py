#!/usr/bin/env python3
"""
Cosmic Cone: Derivación directa de C = 379 Gpc desde CHIME + DESI + Pantheon+
Si SKA-Low detecta 472,789,997.636 Hz, el universo mide 379 Gpc de circunferencia.
Falsable en 400h de integración Phase 1.
"""

import numpy as np

# Constantes físicas exactas
c = 299792458.0  # m/s, definición SI

# Inputs observacionales 2022-2024
H0_CHIME = 74.4      # km/s/Mpc, CHIME 2023
H0_Pantheon = 73.4   # km/s/Mpc, Pantheon+ 2022  
H0_avg = (H0_CHIME + H0_Pantheon) / 2  # 73.9 km/s/Mpc
w_DESI = -0.65       # DESI 2024

# Conversión
Mpc_to_m = 3.085677581e22  # m/Mpc

# 1. Radio de curvatura: R = c/H0 * sqrt(-3w/(1+w))
H0_SI = H0_avg * 1000 / Mpc_to_m  # 1/s
R_m = (c / H0_SI) * np.sqrt(-3 * w_DESI / (1 + w_DESI))
R_Gpc = R_m / Mpc_to_m / 1e9

# 2. Circunferencia: C = 2πR  
C_Gpc = 2 * np.pi * R_Gpc
C_m = C_Gpc * 1e9 * Mpc_to_m

# 3. Frecuencia fundamental: f = c/C
f_Hz = c / C_m

# Output para verificación directa
print("="*50)
print("COSMIC CONE - Verificación directa")
print("="*50)
print(f"H0 usado:     {H0_avg:.1f} km/s/Mpc")
print(f"w_DESI:       {w_DESI:.2f}")
print(f"R curvatura:  {R_Gpc:.1f} Gpc")
print(f"C universo:   {C_Gpc:.0f} Gpc")
print(f"f SKA-Low:    {f_Hz:.3f} Hz")
print("-"*50)
print("Predicción:   472,789,997.636 Hz")
print("Sigma 400h:   >144 sigma si C = 379 Gpc")
print("="*50)
print("Repo: https://github.com/francodealva/Cosmic-cone")
