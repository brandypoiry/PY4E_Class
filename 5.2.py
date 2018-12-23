largest = None
smallest = None

try:
    while True:
        num = int(input("Enter a number: "))
        largest = max(num)
        smallest = min(num)
        if num == "done" : break
except:
    print("Invalid Input")

print("Maximum:", largest)
print("Minimum:", smallest)
