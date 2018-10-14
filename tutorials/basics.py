print("1.Hello World")
name = "World"

print("2.Hello", name)
print("3.Hello "+name)
print("4.Hello", end=" ")
print(name)
print("5.Hello {name}".format(name=name))

name = input("Enter your name:")
print("6.Hello, {name}".format(name=name))

principal = -1
while principal < 0:
    try:
        principal = float(input("Enter Loan Amount: "))
    except ValueError:
        print("Invalid Loan Amount")
        principal = -1
interest = 3.0
periods = 12
n_years = 32

final_cost = principal * (1 + ((interest/100.0)/periods))**(periods*n_years)

print(final_cost)
print("{cost:0.02f}".format(cost=final_cost))
print("Total Interest Paid: {interest:0.02f}".format(interest=final_cost-principal))
print("Monthly Payments: {payment:0.02f}".format(payment=final_cost/(12*n_years)))