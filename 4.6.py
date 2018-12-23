def computepay(workedHours, standardRate):
    if hours > 40:
        standardPay = 40*rate
        overTimePay = (hours-40)*(1.5*rate)
        pay = standardPay+overTimePay
    else:
        pay = hours*rate
    return pay


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
totalPay = computepay(hours, rate)

print(totalPay)
