'''
Formula: Simple Interest (SI) = (Principal x Interest Rate x Time) / 100
Formula: Compound Interest (CI) = P * (1 + r/n)^(nt) - P 

Principal amount (P): The initial amount of money borrowed or invested. 
Interest rate (r): The percentage rate charged on the loan or paid on the investment 
Time (t): The duration of the loan or investment period 
Compounding frequency (n): How often interest is calculated and added to the principal within a given time period (e.g., annually, semi-annually, quarterly '''
p = float(input("Enter principal: "))
ir = float(input("Interest rate: "))
t = float(input("Time: "))
n = float(input("Compound frequency: "))
SI = (p*ir*t)/100
print("Simple Interest: ",SI)
CI = p*(1+ir/n)**(n*t) - p
print("Compound Interest: ",CI)
