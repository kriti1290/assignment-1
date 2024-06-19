while True:

    choice = input("Enter '1' to convert Celsius to Fahrenheit, '2' to convert Fahrenheit to Celsius, or 'q' to quit: ").strip().lower()

    if choice == '1':
       
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    elif choice == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter '1', '2', or 'q'.")

