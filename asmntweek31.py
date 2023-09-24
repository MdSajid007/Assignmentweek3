try:

    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * 1.5 * rate 

    print("Salary: $%s" %salary)
    
except ValueError:
    print("Error: Please enter proper numeric input.")
  
