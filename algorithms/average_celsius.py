def average_celsius(fahrenheit_readings):
    celsius_reading = []
    sum = 0
    
    for i in range(len(fahrenheit_readings)):
        celsius_conversion = (fahrenheit_readings[i] - 32)/1.8
        celsius_reading.append(celsius_conversion)
    
    for i in celsius_reading:
        sum += i
    return sum / len(celsius_reading)

print(average_celsius([134, 82, 109, 32, 210, 134]))
