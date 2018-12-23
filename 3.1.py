hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    overtime = float(hours-40)
    pay = (40*rate)+(overtime*1.5*rate)
else: pay = hours*rate

print pay
