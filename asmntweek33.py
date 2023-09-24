count = 0
total = 0

while True:
    input_number = input("Enter a number: ")

    if input_number == 'done':
        
        break

    try:
        number = float(input_number)
        count = count + 1
        total = total + number
    except ValueError:
        print("Invalid input. Enter a number.")

if count > 0:
    average = total / count
    print("Sum of input numbers: %s" %total)
    print("Number of input: %s" %count)
    print("Average of input numbers: %s" %average)
else:
    print("No valid numbers entered.")


