def main():
    # Prompt the user for mass in kilograms (convert input string to integer)
    mass = int(input("m: "))
    
    # Calculate energy (E = m * c^2)
    energy = calculate_energy(mass)
    
    # Output the result
    print(f"E: {energy}")


def calculate_energy(m):
    # Speed of light in meters per second
    c = 300000000
    
    # Return energy (m * c squared)
    return m * (c ** 2)


if __name__ == "__main__":
    main()