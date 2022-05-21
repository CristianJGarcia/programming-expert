while True:
    num = input("Enter a number: ")

    try:
        num = float(num)
        break
    except ValueError:
        print("Not a valid float, try again!")