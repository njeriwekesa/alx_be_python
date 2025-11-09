income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
savings = income - expenses 
projectedAnnualSavings = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projectedAnnualSavings}.")

