print("DIVISION PROGRAM")
while True:
    try:
        x = float(input("Enter first value: "))
        y = float(input("Enter second value: "))
        result = x/y
        print(f"-Result: {x} / {y} = {result}")
        break
    except ValueError:
        print("Invalid input. Only numeric values allowed")
    except ZeroDivisionError:
        print("Cannot divide by zero. second value must be greater than zero")