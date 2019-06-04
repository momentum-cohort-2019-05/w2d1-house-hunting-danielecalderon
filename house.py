annual_salary = int(input("What is your Anuunal Salary?"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))


#portion_down_payment = .25
portion_down_payment = total_cost * .25
current_savings = 0
r = .04

number_months = 0
 
while (portion_down_payment >= current_savings):
    current_savings = (current_savings + (current_savings * (r/12))) + ((annual_salary/12) * portion_saved)
    number_months += 1


print ("Enter your annual salary:", annual_salary)
print("Enter the percent of your salary to save, as a decimal:", portion_saved)
print("Enter the cost of your dream home:", total_cost)
print("Number of months:", number_months)

