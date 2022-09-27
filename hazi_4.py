def divide(num1, num2):
    
    try:
        a = num1 / num2
        print(round(a, 2))
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally: 
        print("Out of try except blocks")

while True:
    anum = float(input("Enter 'a' value: "))
    bnum = float(input("Enter 'b' value: "))
    divide(anum, bnum)