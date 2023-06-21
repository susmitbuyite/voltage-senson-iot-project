import serial

ser = serial.Serial('COM8', 9600) # replace 'COM7' with the port your Arduino is connected to

while True:
    # Wait for the Arduino to send a line of text
    line = ser.readline().decode(encoding='cp1252').strip()


    # Check if the line contains the voltage value
    if line.startswith("Voltage is : "):
        voltage = float(line[len("Voltage is : "):])
        print(f"Voltage: {voltage:.2f} V")
