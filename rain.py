def input_opinion() -> tuple[int, int]:
    while True:
        try:
            rain = int(input("Enter your opinion if it will rain (from 1 to 10): "))
            if rain < 1 or rain > 10:
                raise ValueError("Opinion must be between 1 and 10.")
            not_rain = int(input("Enter your opinion if it will not rain (from 1 to 10): "))
            if not_rain < 1 or not_rain > 10:
                raise ValueError("Opinion must be between 1 and 10.")
            return (rain, not_rain)
        except ValueError:
            print("Invalid input. Please enter integers between 1 and 10.")

def utility_calculation(prob: float, op: tuple[int, int]) -> float:
    return prob * op[0] + (1 - prob) * op[1]

def main():
    while True:
        try:
            prain = float(input("Enter probability of rain (P(rain)): "))
            if prain < 0 or prain > 1:
                raise ValueError("Probability must be between 0 and 1.")
            break
        except ValueError:
            print("Invalid input. Please enter a float between 0 and 1.")
    print("\nIf staying home")
    home = input_opinion()
    print("\nIf going to the forest")
    forest = input_opinion()
    whome = utility_calculation(prain, home)
    wforest = utility_calculation(prain, forest)
    print(f"\nUtility of staying home: {whome:.2f}")
    print(f"Utility of going to the forest: {wforest:.2f}")
    print("\nRecommendation:")
    if whome > wforest:
        print("You should stay home.")
    elif whome < wforest:
        print("You should go to the forest.")
    else:
        print("Can't recommend. Decide by yourself.")

if __name__ == "__main__":
    main()