import cmath

def z_transform_unit_step():
    # Z-transform of u[n]: U(z) = z / (z - 1)
    print("Z-transform U(z) = z / (z - 1)")

    # Denominator z - 1 = 0 -> pole at z = 1
    pole = 1 + 0j
    print("Pole:", pole)

    # Stability check: |pole| < 1 ? 
    if abs(pole) < 1:
        print("System is Stable")
    else:
        print("System is Unstable")

z_transform_unit_step()
