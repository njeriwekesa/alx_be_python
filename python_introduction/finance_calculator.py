income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
savings = income - expenses 
projectedAnnualSavings = savings * 12 + (savings * 12 * 0.05)

print(savings)
print("Projected savings, after one year, with interest is:", projectedAnnualSavings)
