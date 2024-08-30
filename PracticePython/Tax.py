def calculate_tax(annual_income):
    if annual_income <= 300000:
        tax = 0
    elif annual_income <= 700000:
        tax = (annual_income - 300000) * 0.05
    elif annual_income <= 1000000:
        tax = (700000 - 300000) * 0.05 + (annual_income - 700000) * 0.10
    elif annual_income <= 1200000:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (annual_income - 1000000) * 0.15
    elif annual_income <= 1500000:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (1200000 - 1000000) * 0.15 + (annual_income - 1200000) * 0.20
    else:
        tax = (700000 - 300000) * 0.05 + (1000000 - 700000) * 0.10 + (1200000 - 1000000) * 0.15 + (1500000 - 1200000) * 0.20 + (annual_income - 1500000) * 0.30

    return tax

def main():
    try:
        annual_income = float(input("Enter your annual income: "))
        if annual_income < 0:
            print("Annual income cannot be negative.")
            return

        tax = calculate_tax(annual_income)
        print(f"The calculated income tax is: {tax}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
