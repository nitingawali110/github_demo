def calculate_tax(income):
    # Define tax slabs and rates
    tax_slabs = [(0, 300000, 0.00), (300001, 700000, 0.05),
                 (700001, 1000000, 0.10), (1000001, 1200000, 0.15),
                 (1200001, 1500000, 0.20), (1500001, float('inf'), 0.30)]

    # Standard deduction
    standard_deduction = 75000

    # Calculate taxable income
    taxable_income = max(0, income - standard_deduction)

    # Calculate tax based on slabs
    tax = 0.0
    for lower_limit, upper_limit, rate in tax_slabs:
        if taxable_income > lower_limit:
            taxable_income_in_slab = min(taxable_income, upper_limit) - lower_limit
            tax += taxable_income_in_slab * rate
        else:
            break

    return tax

# Earnings and deductions
monthly_earnings = 80941
annual_earnings = monthly_earnings * 12

# Total deductions (excluding TDS)
annual_deductions = 4300 * 12

# Calculate gross annual income
gross_annual_income = annual_earnings - annual_deductions

# Calculate tax
tax_liability = calculate_tax(gross_annual_income)

print(f"Annual Earnings: ₹{annual_earnings}")
print(f"Annual Deductions: ₹{annual_deductions}")
print(f"Gross Annual Income: ₹{gross_annual_income}")
print(f"Taxable Income: ₹{gross_annual_income - 75000}")
print(f"Tax Liability (New Regime): ₹{tax_liability:.2f}")
