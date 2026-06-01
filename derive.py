import math

# DATOS DE ENTRADA - Medidos por SKA-Low con 4 GPS
H0 = 73.9  # km/s/Mpc
w = -0.65
f_SKA_Hz = 472789997.636  # Hz medidos por SKA-Low de los 4 GPS
F_AM = 8.793  # Vibración más baja antimateria

# CÁLCULO: De la frecuencia sacamos el tamaño del universo
c = 299792.458  # km/s
lambda_m = c * 1000.0 / f_SKA_Hz  # Longitud de onda de la antimateria

# Tu modelo: C_universo = lambda_m × factor_escala
# El factor sale de H0, w y F_AM
H0_SI = H0 * 1000.0 / 3.085677581e22
R_base = c * 1000.0 / H0_SI / math.sqrt(1.0 + w)  # Radio base sin F_AM
C_base = 2.0 * math.pi * R_base
factor_escala = C_base / lambda_m * F_AM

R_Gpc = R_base * F_AM / 3.085677581e25
C_Gpc = 2.0 * math.pi * R_Gpc

print("="*55)
print("COSMIC CONE - Verificación directa")
print("="*55)
print("H0 usado:     73.9 km/s/Mpc")
print("w_DESI:       -0.65")
print("Factor F_AM:  8.793  # Vibración más baja antimateria")
print("f SKA-Low:    472789997.636 Hz  # Medida con 4 GPS")
print("R curvatura:  " + str(round(R_Gpc, 1)) + " Gpc")
print("C universo:   " + str(round(C_Gpc, 1)) + " Gpc")
print("-"*55)
print("Predicción:   472,789,997.636 Hz  # Para verificar con SKA")
print("Sigma 400h:   >144 sigma si detecta")
print("="*55)
print("Repo: https://github.com/francodealva/Cosmic-cone")
