import dis

def magic_calculation(a, b):
    return 98 + (a ** b)

# Verify that the bytecode matches the given specifications
dis.dis(magic_calculation)
