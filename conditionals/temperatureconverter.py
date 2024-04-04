def temperature_converter():
    temperature = float(input("Enter temperature: "))
    scale = input("Enter scale (C for Celsius, F for Fahrenheit): ")

    if scale.upper() == 'C':
        converted_temp = (temperature * 9/5) + 32
        print("Converted temperature:", converted_temp, "F")
    elif scale.upper() == 'F':
        converted_temp = (temperature - 32) * 5/9
        print("Converted temperature:", converted_temp, "C")
    else:
        print("Invalid scale!")

temperature_converter()
